/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    git url: 'https://github.com/Abhishekkanawade20/My-Webpage.git', branch: 'main'
                }
            }
        }
    }
}
