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
                sh 'pip3 install -r app/requirements.txt'
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
