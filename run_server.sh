# This will build and excecute the docker container
sh build_server.sh &&
sh generate_cert.sh &&
echo "\n\tStarting Container...\n" &&
docker run --rm -p 127.0.0.1:50051:50051 -v $(pwd)/secret:/secret ml-ms-ml-backend
