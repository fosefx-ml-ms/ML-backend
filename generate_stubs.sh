# Executing this file will generate new stubs based on the prototype buffers in ./proto
# This will run everytime you run ./build_server or ./run_server
echo "\n\tGenerating Stubs...\n" &&
docker build -t ml-ms-ml-backend-builder -f stage1.Dockerfile . &&
docker run --rm -v $(pwd)/src:/out ml-ms-ml-backend-builder
