sh build_server.sh &&
mv Dockerfile Dockerfile_tmp &&
mv Dockerfile_debug Dockerfile &&
docker build -t ml-ms-ml-client . &&
mv Dockerfile Dockerfile_debug &&
mv Dockerfile_tmp Dockerfile