pipeline {
    agent any

    stages {

        stage('Debug Docker') {
            steps {
                bat '''
                    set "PATH=C:\\Users\\SHAKSHI\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%"
                    where docker
                    docker --version
                    docker info
                '''
            }
        }

        stage('Checkout') {
            steps {
                echo 'Checking out GitHub repository...'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker images...'
                bat 'docker compose build'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Starting Docker containers...'
                bat 'docker compose up -d'
            }
        }

        stage('Check Containers') {
            steps {
                echo 'Checking containers...'
                bat 'docker compose ps'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL - Docker containers are running!'
        }

        failure {
            echo 'BUILD FAILED - Check the console output.'
        }
    }
}
