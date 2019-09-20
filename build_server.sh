# This will build the docker container
sh generate_stubs.sh &&
echo "\n\tBuilding Container\n" &&
docker build -t ml-ms-ml-backend -f stage2.Dockerfile .
