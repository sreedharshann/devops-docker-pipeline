pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container devops-flask-app'
            }
        }

    }
}