# Jenkins CI/CD Deployment Project

This project demonstrates:
GitHub -> Jenkins -> Docker Build -> Docker Hub -> AWS EC2 -> Docker Container -> Flask Application

## Files
- app.py - Flask application
- requirements.txt - Python dependency
- Dockerfile - Container image definition
- Jenkinsfile - CI/CD pipeline
- .dockerignore - Docker build exclusions

## Before running
Edit Jenkinsfile:
1. Replace YOUR_DOCKERHUB_USERNAME
2. Replace YOUR_13.232.74.227

Do not commit passwords, tokens, AWS keys, or SSH private keys.
