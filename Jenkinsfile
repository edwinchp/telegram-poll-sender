pipeline {
    agent any
    
    environment {
        VENV_PATH = "${WORKSPACE}/venv"
        PYTHON = "${VENV_PATH}/bin/python"
        PIP = "${VENV_PATH}/bin/pip"
    }
    
    stages {
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv ${VENV_PATH}
                    ${PIP} install --upgrade pip
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    ${PIP} install -r requirements.txt
                '''
            }
        }
        
        stage('Run Application') {
            steps {
                withCredentials([
                    string(credentialsId: params.BOT_TOKEN, variable: 'BOT_TOKEN'),
                    string(credentialsId: params.CHAT_ID, variable: 'CHAT_ID')
                ]) {
                    sh '''
                        export BOT_TOKEN=$BOT_TOKEN
                        export CHAT_ID=$CHAT_ID
                        ${PYTHON} main.py
                    '''
                }
            }
        }
    }
    
    post {
        always {
            deleteDir()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}