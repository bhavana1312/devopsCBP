pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/bhavana1312/devopsCBP.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-cicd-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker rm -f flask-cicd-app-container || true'
                    sh 'docker run -d -p 5000:5000 --name flask-cicd-app-container flask-cicd-app'
                }
            }
        }
    }
}
