pipeline {
    agent any
    
    stages {
  
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
                script {
                    // Enclose shell steps in curly braces
                    sh 'cp /var/lib/jenkins/workspace/newP/*.html /var/www/html/'
                    sh 'systemctl restart nginx'
                }
            }
        }
    }
}

