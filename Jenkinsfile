pipeline {
    agent any

    stages {

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
                sh 'docker build -t nimbus-tasks:latest .'
            }
        }

        stage('Verify Image') {
            steps {
                sh '''
                    docker image inspect nimbus-tasks:latest > /dev/null
                    echo "NimbusTasks image verified successfully!"
                '''
            }
        }
    }
}
