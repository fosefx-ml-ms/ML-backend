# ML-backend
This microservice is responsible for the classification of the images.

Image taken from:
https://pixabay.com/photos/book-embossing-leather-book-cover-3088775/

## Scripts
> Linux and Mac only
* Run `./run_server.sh` to generate new stubs, to build the container and to run it
* Run `./build_server.sh` to generate new stubs and to build the container
* Run `./generate_stubs.sh` to generate new stubs based on `./protos/ml.proto`
* Run `./clean.sh` ro remove all docker containers and images
* Run `./generate_cert.sh` generates a new SSL-keypair  (requires OpenSSL)
* Run `./run_client.sh` to build and run client.py

## K8s-Deployment

1. If not done yet, create the ml-ms namespace:
  `kubectl create namespace ml-ms`
2. Build and push container: 
  ```
  $ ./build_server.sh
  $ docker tag ml-ms-ml-backend:latest <yourdockerhubname>/ml-ms-ml-backend:<version>
  $ docker push <yourdockerhubname>/ml-ms-ml-backend:<version>
  ```
> Make sure you replace "localhost" with your services hostname in "generate_cert.sh" before deploying.
3. Generate certificate: `./generate_cert.sh`
4. Create Certificate-Secret: `kubectl create secret generic grcp-ml-certificate --namespace=ml-ms --from-file=./secret/certificate.crt --from-file=./secret/key.pem`
5. Edit k8s.yml and replace the image with yours
6. deploy: `kctl apply -f k8s.yml`