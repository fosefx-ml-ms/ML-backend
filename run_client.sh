sh build_server.sh &&
docker build -t ml-ms-ml-client -f client.Dockerfile . &&
sh generate_cert.sh &&
docker run --rm -ti --network=host -v $(pwd)/secret:/secret ml-ms-ml-client