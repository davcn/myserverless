pipeline {
	agent none
    stages {
	    stage('test') {
		    agent { dockerfile true }
	        steps {
				sh 'pytest test_dynamodb.py'
	        }
		    post {
		    	always {
			    archiveArtifacts artifacts: '*.py', fingerprint: true
		    	}
		    }
		}
		stage('deploy') {
    		agent { 
    			dockerfile {
                    dir 'serverless/'
                }
            }
            steps {
				echo "AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID}\nAWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY}" >> .aws/credentials
            	sh 'sls deploy'
            }
	    }
    }
}
