pipeline {
    agent any
    
    environment {
        VENV_PATH = "${WORKSPACE}/venv"
        PYTHON = "${VENV_PATH}/bin/python"
        PIP = "${VENV_PATH}/bin/pip"
    }
    
    stages {
        stage('Load Environment') {
            steps {
                script {
                    def envFile = params.ENV_FILE
                    if (!fileExists(envFile)) {
                        error "Environment file ${envFile} not found"
                    }
                    def props = readProperties file: envFile
                    props.each { key, value ->
                        env[key] = value
                    }
                }
            }
        }
        
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