pipeline {
    agent any // This specifies that the pipeline can run on any available agent.
   
    stages {
        stage('Build') {
            steps {
                //  build project.
                sh 'echo "Building the project..."'
            }
        }

        stage('Run Pytest and Codecov') {
            environment { //sets environment for pytest and codecov to run
                CODECOV_TOKEN = credentials('CODECOV_TOKEN_sprint2')
            }
            steps {
                // run tests.
                sh 'echo "Running tests..."'
                script {
                    sh 'pytest --cov=my_application --cov-report=term tests/'
                    sh 'codecov -t $CODECOV_TOKEN -b ${BRANCH_NAME}'
                }
            }
        }
    }

    post {
        success {
            // This block is executed if the pipeline runs successfully.
            echo 'Pipeline succeeded! Your project is built and tested.'
        }
        failure {
            // This block is executed if the pipeline fails.
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}