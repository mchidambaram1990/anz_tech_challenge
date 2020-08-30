pipeline {



  agent any
  parameters {
  	choice(name: 'action', choices: 'create\nrollback', description: 'Create/rollback of the deployment')
    string(name: 'ImageName', description: "Name of the docker build")
  	string(name: 'ImageTag', description: "Name of the docker build")
  	string(name: 'AppName', description: "Name of the Application")
    string(name: 'docker_repo', description: "Name of docker repository")
    }

  stages {
    stage('checkout') {
        when {
        				expression { params.action == 'create' }
        			}
        steps {
            git 'https://github.com/mchidambaram1990/testpy.git'
        }
    }
    stage('docker build') {
        when {
        				expression { params.action == 'create' }
        			}
        steps {
         	dir("${params.AppName}") {
         	    dockerBuild ( "${params.ImageName}", "${params.docker_repo}" )
         	}
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