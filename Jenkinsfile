pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sign-language-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f sign-language-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                --name sign-language-app \
                -p 5000:5000 \
                sign-language-app:latest
                '''
            }
        }

    }
}