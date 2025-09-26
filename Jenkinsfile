/* groovylint-disable CompileStatic */
pipeline {
    agent any 

    stages {
        stage('Checkout Code from GitHub') {
            steps {
                // Use SSH to authenticate
                git branch: 'main',
                    url: 'git@github.com:Abhishekkanawade20/My-Webpage.git',
                    credentialsId: 'Abhishekkanawade20'
            }
        }
    }
}