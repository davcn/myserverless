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
            environment {
        		AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        		AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    		}
            steps {
				sh '''
					ls -la /home
					ls -la /home/serverless
					ls -la /home/serverless/.aws
					echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" >> /home/serverless/.aws/credentials
					echo "AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY" >> /home/serverless/.aws/credentials
            		sls deploy
            	'''
            }
	    }
    }
}
