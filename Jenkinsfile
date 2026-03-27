pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t flask-app . > build.log 2>&1 || true
                '''
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

                script {
                    // Save last 100 lines of console logs
                    def logs = currentBuild.rawBuild.getLog(100).join("\n")
                    writeFile file: 'build.log', text: logs
                }

                // Activate venv and run Ollama script
                sh '''
                    source /opt/venv/bin/activate
                    python3 error.py build.log
                '''
            }
        }
    }
}
