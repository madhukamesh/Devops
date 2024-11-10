Docker Commands
===============

build : docker build . -t image_name:version

run :
    basic - to run the image
        docker run image_name:version

    server - to run in different port numbers
        docker run -p <os-port>:<container-port> image_name:version


docker file name: docker build . -f docker_file_name -t image_name:version

default docker file name : Dockerfile




docker build : Looks for default : Dockerfile
docker compose : Looks for default : compose.yaml