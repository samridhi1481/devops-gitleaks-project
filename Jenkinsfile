pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/samridhi1481/devops-gitleaks-project.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t attendance-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run attendance-app'
            }
        }
    }
}