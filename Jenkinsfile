pipeline {
    agent any 
    
    stages {
        stage('checkout code from Github') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Abhishekkanawade20/My-Webpage.git'
                    credentialsId: 'github-https'
            }
        }
    }
}
