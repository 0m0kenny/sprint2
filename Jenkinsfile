pipeline {
    agent any // This specifies that the pipeline can run on any available agent.
    environment {
        CODECOV_TOKEN = credentials('CODECOV_TOKEN_sprint2')
    }
    stages {
        stage('Build') {
            steps {
                //  build project.
                sh 'echo "Building the project..."'
            }
        

        stage('Run Pytest and Codecov') {
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