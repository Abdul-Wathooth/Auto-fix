pipeline {
    agent any

    environment {
        OPENAI_API = "https://api.openai.com/v1/chat/completions"
    }

    stages {

        stage('Build Image') {
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
            script {

                echo "❌ Build failed. Sending logs to AI..."

                def logs = currentBuild.rawBuild.getLog(100).join("\n")

                writeFile file: 'error.log', text: logs

                withCredentials([string(credentialsId: 'openai-api-key', variable: 'OPENAI_KEY')]) {

                    sh """
                    curl -s ${OPENAI_API} \\
                      -H "Content-Type: application/json" \\
                      -H "Authorization: Bearer $OPENAI_KEY" \\
                      -d '{
                        "model": "gpt-4o-mini",
                        "messages": [
                          {
                            "role": "system",
                            "content": "You are a DevOps + Python expert. Find root cause and fix."
                          },
                          {
                            "role": "user",
                            "content": "Flask Docker build failed. Logs:\\n${logs}"
                          }
                        ]
                      }' > ai-response.json
                    """

                    echo "🤖 AI Response:"
                    sh "cat ai-response.json"
                }
            }
        }
    }
}
