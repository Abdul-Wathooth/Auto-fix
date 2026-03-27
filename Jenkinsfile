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
            echo "Build failed! Running error handler..."

            sh '''
            echo "Sending logs to AI..."

            python3 error.py build.log
            '''
        }
    }
}
