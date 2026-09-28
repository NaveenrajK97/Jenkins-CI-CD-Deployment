pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "naveenrajk3/jenkins-cicd"
        DOCKER_TAG = "${BUILD_NUMBER}"

        DOCKER_CREDENTIALS = "dockerhub-credentials"
        EC2_CREDENTIALS = "ec2-ssh-key"

        EC2_USER = "ec2-user"
        EC2_HOST = "13.232.74.227"

        CONTAINER_NAME = "jenkins-cicd-app"

        PYTHON = "C:\\Users\\navee\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing application dependencies...'

                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m pip --version
                    "%PYTHON%" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests...'

                bat '''
                    "%PYTHON%" -m py_compile app.py
                    echo Application syntax test passed
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'

                bat '''
                    docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% .
                    docker tag %DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_IMAGE%:latest
                '''
            }
        }

        stage('Docker Login & Push') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'

                withCredentials([
                    usernamePassword(
                        credentialsId: "${DOCKER_CREDENTIALS}",
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    bat '''
                        echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                        docker push %DOCKER_IMAGE%:%DOCKER_TAG%
                        docker push %DOCKER_IMAGE%:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                echo 'Deploying application to EC2...'

                sshagent(credentials: ["${EC2_CREDENTIALS}"]) {
                    bat '''
                        ssh -o StrictHostKeyChecking=no %EC2_USER%@%EC2_HOST% "docker pull %DOCKER_IMAGE%:latest"
                        ssh -o StrictHostKeyChecking=no %EC2_USER%@%EC2_HOST% "docker stop %CONTAINER_NAME% || true"
                        ssh -o StrictHostKeyChecking=no %EC2_USER%@%EC2_HOST% "docker rm %CONTAINER_NAME% || true"
                        ssh -o StrictHostKeyChecking=no %EC2_USER%@%EC2_HOST% "docker run -d --name %CONTAINER_NAME% -p 8080:8080 %DOCKER_IMAGE%:latest"
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying application deployment...'

                sshagent(credentials: ["${EC2_CREDENTIALS}"]) {
                    bat '''
                        ssh -o StrictHostKeyChecking=no %EC2_USER%@%EC2_HOST% "docker ps"
                        ssh -o StrictHostKeyChecking=no %EC2_USER%@%EC2_HOST% "docker logs --tail 20 %CONTAINER_NAME%"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI/CD PIPELINE COMPLETED SUCCESSFULLY!'
            echo "Application URL: http://${EC2_HOST}:8080"
        }

        failure {
            echo 'CI/CD PIPELINE FAILED - Check Console Output.'
        }
    }
}