pipeline {



  agent any
  environment {
      registry = "mchidambaram1990/anz"
      registryCredential = ‘dockerhub’
      dockerImage = ''
  }

  stages {
    stage('checkout') {

        steps {
            git 'https://github.com/mchidambaram1990/testpy.git'
        }
    }
    stage('docker build') {

        steps {
          script {
            docker rmi anz
            dockerImage = docker build -t anz .
            }
          }
        }
     stage("Docker push to hub") {
     	 steps {
     	     script {
                 docker.withRegistry( '', registryCredential ) {
                   dockerImage.push()
                 }
     		 }
     	 }
     }
  }
}