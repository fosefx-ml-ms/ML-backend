# this file is used for debugging
import grpc
import ml_pb2
import ml_pb2_grpc

if __name__ == '__main__':
    with open('../secret/certificate.crt', 'rb') as cert_file:
        ssl_creds = grpc.ssl_channel_credentials(root_certificates=cert_file.read())

    with grpc.secure_channel('localhost:50051', ssl_creds) as channel:
        stub = ml_pb2_grpc.MLBackendStub(channel)
        with open("src/img.jpg", "rb") as image:
            f = image.read()
        b = bytearray(f)
        print(stub.ClassifyImage(ml_pb2.ImageClassificationRequest(image=bytes(b))))
