#!/bin/bash
# Build the Docker image
docker build -t ranking-search-engine_web .

# Run the Docker container
docker run -d --name fastapi-container -p 8000:80 ranking-search-engine_web

