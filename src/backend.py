from concurrent import futures
import time
import random
import logging
import sys
import grpc
import ml_pb2
import ml_pb2_grpc
import torch
from fastai import *
from fastai.vision import *

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MLServicer(ml_pb2_grpc.MLBackendServicer):
    def __init__(self):
        logging.debug("Initializes MLServicer")
        defaults.device = torch.device('cpu')
        self.learner = load_learner(Path(".."))
        logging.debug("MLServicer initialized")

    def ClassifyImage(self, request, context):
        logging.debug("ClassifyImage called")
        
        img_bytes = request.image
        
        img = open_image(BytesIO(img_bytes))
        
        pred_class, pred_index, probabilities = self.learner.predict(img)
        logging.debug((pred_class, pred_index, probabilities))
        
        index = pred_index.item()
        confidence = probabilities[index].item()
        logging.debug(confidence)

        class_readable = pred_class.obj.upper()
        logging.info("Detected class {} with {} confidence".format(class_readable, confidence))

        return ml_pb2.ImageClassificationResponse(resultReadable=class_readable)

def get_certificate():
    try:

        with open('../secret/key.pem', 'rb') as f:
            private_key = f.read()
        with open('../secret/certificate.crt', 'rb') as f:
            certificate = f.read()
        
        return grpc.ssl_server_credentials(((private_key, certificate,),))


    except FileNotFoundError as e:
        logging.debug("FileNotFound when trying to load certificate: {}".format(e))
        logging.critical("Certificate Files not found")
        sys.exit(0)

if __name__ == '__main__':
    
    # initializes logging
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting server...")
    
    # gRPC server instance, not listening yet
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # add MLServicer to server
    ml_pb2_grpc.add_MLBackendServicer_to_server(MLServicer(), server)

    # starts listening on SSL port
    ssl_creds = get_certificate()
    server.add_secure_port('[::]:50051', ssl_creds)
    server.start()

    # keeping main thread busy, so it can not shut down
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)