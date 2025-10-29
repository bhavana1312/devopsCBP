pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/bhavana1312/devopsCBP.git', branch: 'main'
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker rm -f flask-app-container || true'
                sh 'docker run -d --name flask-app-container -p 5000:5000 flask-app'
            }
        }
    }
}
