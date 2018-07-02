pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('build') {
            steps {
                sh 'python computeFn.py'
            }
        }
    }
}
