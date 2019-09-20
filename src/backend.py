from concurrent import futures
import time
import grpc
import ml_pb2
import ml_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MLServicer(ml_pb2_grpc.MLBackendServicer):
    def ClassifyImage(self, request, context):
        print("Called")
        print(self)
        print(request)
        print(context)
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