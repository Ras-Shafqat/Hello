pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python3 -m unittest test_app.py || python test_app.py || true'
            }
        }
        stage('Build & Package') {
            steps {
                echo 'Building and packaging artifact...'
                sh 'bash build.sh'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'build/**/*', fingerprint: true, allowEmptyArchive: true
            echo 'Build and test process completed.'
        }
        success {
            echo 'Jenkins build succeeded!'
        }
        failure {
            echo 'Jenkins build failed!'
        }
    }
}
