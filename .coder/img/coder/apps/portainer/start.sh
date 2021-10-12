#!/bin/bash

docker run -d \
    --publish=8000:8000 \
    --publish=9000:9000 \
    --name=portainer \
    --volume=/var/run/docker.sock:/var/run/docker.sock \
    --restart=always \
    --volume=portainer_data:/home/portainer/data \
    portainer/portainer-ce:latest
