# this file is used for debugging
import grpc
import ml_pb2
import ml_pb2_grpc

if __name__ == '__main__':

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ml_pb2_grpc.MLBackendStub(channel)
        with open("src/img.jpg", "rb") as image:
            f = image.read()
            b = bytearray(f)
            print(stub.ClassifyImage(ml_pb2.ImageClassificationRequest(image=bytes(b))))
