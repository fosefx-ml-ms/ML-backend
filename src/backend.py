from concurrent import futures
import time
import random
import grpc
import ml_pb2
import ml_pb2_grpc
from fastai import *
from fastai.vision import *

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MLServicer(ml_pb2_grpc.MLBackendServicer):
    def __init__(self):
        self.learner = load_learner(Path("export.pkl"))
        self.id = random.randint(0, 10000)
        print("Done initializing " + self.id)
    
    def ClassifyImage(self, request, context):
        print("Called")
        img_bytes = request.image
        img = open_image(BytesIO(img_bytes)))
         _,_,losses = self.learner.predict(img)
        print(losses)
        return ml_pb2.ImageClassificationResponse(resultReadable="UNKNOWN")


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ml_pb2_grpc.add_MLBackendServicer_to_server(MLServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)