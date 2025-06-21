#!/bin/sh

# Create the readings folder if it doesn't exist
mkdir -p readings

# Run the Docker container
docker run --rm -it \
  --name save-server \
  -p 5000:5000 \
  -v "$(pwd):/app" \
  save-server:latest

