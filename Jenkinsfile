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
    			docker {
                	reuseNode true
                	image 'node'
                }
            }
            steps {
            	sh 'npm i'
            }
	    }
    }
}
