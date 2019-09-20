FROM ml-ms-ml-backend-builder
COPY export.pkl export.pkl
COPY protos protos
RUN rm out -rf
COPY src src
RUN rm src/img.jpg
RUN rm src/client.py
CMD [ "/opt/conda/bin/python", "src/backend.py" ]
