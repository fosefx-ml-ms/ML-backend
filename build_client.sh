docker build -t ml-ms-ml-backend . &&
mv Dockerfile Dockerfile_tmp &&
mv Dockerfile_debug Dockerfile &&
docker build -t ml-ms-ml-client . &&
mv Dockerfile Dockerfile_debug &&
mv Dockerfile_tmp Dockerfile &&
docker run --rm -ti --network=host ml-ms-ml-client
