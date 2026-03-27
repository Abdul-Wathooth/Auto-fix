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
                    def logs = currentBuild.rawBuild.getLog(100).join("\n")
                    writeFile file: 'error.log', text: logs
                }

                sh '''
                    source /opt/venv/bin/activate"
                    python3 error.py build.log
                '''
        }
    }
}
