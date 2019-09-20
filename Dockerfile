FROM python:3-alpine as build
RUN apk add --virtual .build-deps g++ python3-dev libffi-dev openssl-dev
RUN pip3 install --upgrade pip setuptools
RUN pip3 install grpcio-tools
RUN pip3 install fastai
COPY protos protos
RUN mkdir src
RUN python -m grpc.tools.protoc -I=protos --python_out=src --grpc_python_out=src protos/ml.proto

COPY src/backend.py src/backend.py
CMD [ "python", "src/backend.py" ]