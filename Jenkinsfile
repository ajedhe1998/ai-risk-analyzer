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
        // stage('Push to Docker Registry') {
        //     steps {
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
        //             sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
        //             sh 'docker push $IMAGE_NAME'
        //         }
        //     }
        // }
    }
}