pipeline {
    agent any
    
    parameters {
        credentials(name: 'BOT_TOKEN', description: 'Telegram bot token', required: true, credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl')
        credentials(name: 'CHAT_ID', description: 'Telegram chat id where poll will be send', required: true, credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl')
        string(name: 'API_LINK', defaultValue: 'http://localhost:8000', description: 'API endpoint to get the questions')
        choice(name: 'API_REQUEST_DIFFICULTY', choices: ['any', 'easy', 'medium', 'hard'], description: 'Question difficulty')
        string(name: 'API_REQUEST_CATEGORY', defaultValue: 'YOUR-CATEGORY', description: 'Question category')
    }
    
    environment {
        VENV_PATH = "${WORKSPACE}/venv"
        PYTHON = "${VENV_PATH}/bin/python"
        PIP = "${VENV_PATH}/bin/pip"
    }
    
    stages {
        
        stage('Setup Python Environment') {
            steps {
                script {
                    sh '''
                        python3 --version
                        python3 -m venv ${VENV_PATH}
                        ${PIP} install --upgrade pip
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        ${PIP} install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Run Application') {
            steps {
                script {
                    sh '''
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