pipeline {
    agent any
    environment {
        IMAGE_NAME = 'your-dockerhub-username/ai-risk-analyzer'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:ajedhe1998/ai-risk-analyzer.git', credentialsId: 'github-ssh-creds'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Login to GHCR') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'ajedhe1998',
                        usernameVariable: 'GITHUB_USER',
                        passwordVariable: 'GITHUB_TOKEN')]) {
                    sh 'echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USER --password-stdin'
                }
            }
        }

        stage('Push Image to GHCR') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }
        
}