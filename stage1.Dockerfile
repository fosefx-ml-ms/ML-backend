FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt


COPY export.pkl export.pkl
COPY protos protos
RUN mkdir out
CMD ["python", "-m", "grpc.tools.protoc", "-I=protos", "--python_out=out", "--grpc_python_out=out", "protos/ml.proto"]
