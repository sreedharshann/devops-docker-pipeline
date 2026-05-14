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
                sh 'docker stop devops-container || true'
                sh 'docker rm devops-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name devops-container -p 5000:5000 devops-flask-app'
            }
        }

    }
}