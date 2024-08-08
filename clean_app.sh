#!/bin/bash
# Clean stack
docker stop fastapi-container
echo "container stopped"
docker rm fastapi-container
echo "container removed"
