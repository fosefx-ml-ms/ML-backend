from concurrent import futures
import time
import random
import logging
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

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ml_pb2_grpc.add_MLBackendServicer_to_server(MLServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)