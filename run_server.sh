# This will build and excecute the docker container
sh build_server.sh &&
echo "\n\tStarting Container...\n" &&
docker run --rm -p 127.0.0.1:50051:50051 ml-ms-ml-backend
