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
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r app/requirements.txt
                    ./venv/bin/pytest
                '''
            }
}

        stage('Build') {
            steps {
                echo 'Building NimbusTasks...'
            }
        }
    }
}
