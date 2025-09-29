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

        stage('Deploy index.html') {
            steps {
                script {
                    // Copy index.html to /var/www/html
                    sh 'cp /var/lib/jenkins/workspace/my-page-production/index.html /var/www/html/'
                }
            }
        }
    }
}
