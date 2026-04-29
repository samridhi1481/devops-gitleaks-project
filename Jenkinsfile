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

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f attendance-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name attendance-container attendance-app'
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

        stage('Ansible Deploy') {
            steps {
                sh 'ansible-playbook playbook.yml'
            }
        }
    }
}
