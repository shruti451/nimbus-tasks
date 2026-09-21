pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
             steps {
                sh 'pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Building NimbusTasks...'
            }
        }
    }
}
