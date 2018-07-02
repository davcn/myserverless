pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python -c \'import computeFn; print computeFn.lambda_handler({"speed":1, "real":3},{})\''
            }
        }
    }
}
