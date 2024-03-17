pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
       
        stage('Test') {
            steps {
                script {
                    // Run Python Selenium script
                    def output = sh(script: 'python3 test_script.py', returnStdout: true).trim()

                    // Check the output to determine the test condition
                    if (output.contains('All tests passed')) {
                        currentBuild.result = 'SUCCESS'
                    } else {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Deployment') {
            steps {
                sh 'sudo cp -r ./*.html /var/www/html/'
                sh 'sudo systemctl restart nginx'
            }
        }
    }
    
   
}
