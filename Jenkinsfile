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
				sh 'pytest test_dynamodb.py'
	        }
		    post {
		    	always {
			    archiveArtifacts artifacts: '*.py', fingerprint: true
		    	}
		    }
		}
    }
}
