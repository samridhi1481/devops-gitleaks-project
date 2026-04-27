pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/samridhi1481/devops-gitleaks-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t attendance-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 attendance-app'
            }
        }
    }
}