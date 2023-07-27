pipeline {
    agent any

    environment {
        EC2_IP = '54.176.142.77'
        EC2_USERNAME = 'ec2-user'
        DOCKER_USERNAME = 'sarthakvengurlekar10'
        DOCKER_IMAGE = 'my_flask_app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                url: 'https://sarthakvengurlekar10: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@github.com/sarthakvengurlekar/FlexionProject.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sarthakvengurlekar10/my_flask_app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -v ${WORKSPACE}:/app -w /app $DOCKER_USERNAME/$DOCKER_IMAGE pytest test_app.py'
            }
        }
        
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    sh 'docker push $DOCKER_USERNAME/$DOCKER_IMAGE'
                }
            }
        }
        


        stage('Deploy') {
            steps {
                sshagent(['ec2-key']) {
                    sh """ssh -o StrictHostKeyChecking=no $EC2_USERNAME@$EC2_IP 'docker stop \$(docker ps -q --filter ancestor=$DOCKER_USERNAME/$DOCKER_IMAGE) || true && docker rm \$(docker ps -a -q --filter ancestor=$DOCKER_USERNAME/$DOCKER_IMAGE) || true && docker pull $DOCKER_USERNAME/$DOCKER_IMAGE:latest && docker run -d -p 5000:5000 $DOCKER_USERNAME/$DOCKER_IMAGE:latest'"""
                }
            }
        }

        
    }
}