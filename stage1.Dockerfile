FROM continuumio/miniconda3:4.7.10-alpine
USER root

RUN apk add --virtual .build-deps g++ python3-dev libffi-dev openssl-dev bash
SHELL ["/bin/bash", "-c"]
RUN /opt/conda/bin/conda init bash
RUN cat /root/.bashrc
RUN /opt/conda/bin/conda create -n myenv python
RUN /opt/conda/bin/conda install -c pytorch -c fastai fastai
RUN /opt/conda/bin/pip install --upgrade pip setuptools
RUN /opt/conda/bin/pip install --upgrade grpcio-tools
RUN source /opt/conda/bin/activate myenv

COPY export.pkl export.pkl
COPY protos protos
RUN mkdir out
CMD ["/opt/conda/bin/python", "-m", "grpc.tools.protoc", "-I=protos", "--python_out=out", "--grpc_python_out=out", "protos/ml.proto"]
