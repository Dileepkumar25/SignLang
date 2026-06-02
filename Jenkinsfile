pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sign-language-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f sign-language-app || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                --name sign-language-app \
                -p 5000:5000 \
                sign-language-app
                '''
            }
        }
    }
}
