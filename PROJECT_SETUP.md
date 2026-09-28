# Setup Checklist

## GitHub
Repository:
https://github.com/NaveenrajK97/Jenkins-CI-CD-Deployment.git
Branch: main

## Docker Hub
Docker Hub repository:
naveenrajk3/jenkins-cicd

## EC2
Install Docker and make sure the Jenkins SSH user can run Docker.

Ubuntu example:
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker ubuntu

## Security Group
Allow SSH 22 and application port 8080 as required.

## Jenkins credentials
Docker Hub:
ID = dockerhub-credentials
Type = Username with password
Password = Docker Hub access token

EC2:
ID = ec2-ssh-key
Type = SSH Username with private key
Username = ubuntu
Private key = your EC2 SSH key

## Jenkins job
Pipeline -> Pipeline script from SCM
SCM = Git
Repository = https://github.com/NaveenrajK97/Jenkins-CI-CD-Deployment.git
Branch = */main
Script Path = Jenkinsfile

## Expected stages
Checkout -> Build -> Test -> Docker Build -> Docker Login & Push -> Deploy to EC2 -> Verify Deployment

## Verification
Open:
http://13.232.74.227:8080
http://13.232.74.227:8080/health
