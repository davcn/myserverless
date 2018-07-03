pipeline {
    agent { dockerfile true }
    stages {
	stage('setup') {
	    steps {
	        sh 'echo setup'
	    }
	}
        stage('test') {
            steps {
		sh '''
		   export AWS_DEFAULT_REGION=us-east-1
		   pytest test_dynamodb.py
		'''
            }
	    post {
	    	always {
		    archiveArtifacts artifacts: '*.py', fingerprint: true
	    	}
	    }
	}
    }
}
