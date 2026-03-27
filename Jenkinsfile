pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        failure {
            steps {
                echo "Build failed! Running error handler..."

                // Save logs
                script {
                    def logs = currentBuild.rawBuild.getLog(100).join("\n")
                    writeFile file: 'error.log', text: logs
                }

                // Call Python script
                sh "python3 error.py error.log"
            }
        }
    }
}
