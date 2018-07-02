pipeline {
    agent { docker { image 'python:2.7' } }
    stages {
        stage('build') {
            steps {
                sh 'python -c \'import computeFn; print computeFn.lambda_handler({"speed":1, "real":3},{})\''
            }
	    post {
	    	always {
		    archive "*.py"
	    	}
	    }
	}
    }
}
