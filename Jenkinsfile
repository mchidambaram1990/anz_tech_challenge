pipeline {



  agent any


  stages {
    stage('checkout') {

        steps {
            git 'https://github.com/mchidambaram1990/testpy.git'
        }
    }
    stage('docker build') {

        steps {
            sh 'docker stop anz'
            sh 'docker rm -f anz'
            sh 'docker image rm -f anz'
         	sh 'docker build -t anz .'
         	}
        }
     stage("Docker CleanUP") {
     	 when {
     				    expression { params.action == 'create' }
     			   }
     	 steps {
     	        dockerCleanup ( "${params.ImageName}", "${params.docker_repo}" )
     		 }
     	 }
  }
}