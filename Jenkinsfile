pipeline{

  agent any
  parameters {
  	choice(name: 'action', choices: 'create\nrollback', description: 'Create/rollback of the deployment')
  }
  environment {
      registry = "mchidambaram1990/anz"
      registryCredential = 'dockerhub'
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
             dockerImage = docker.build registry + ":latest"
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
     stage("Create deployment")
     {
        when {
              expression { params.action == 'rollback' }
        }
         steps
         {
             withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                   accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                   credentialsId: 'AWS_Credentials',
                   secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
                 {
                    withCredentials([kubeconfigFile(credentialsId: 'kubernetes_config',
                    variable: 'KUBECONFIG')])
                    {
                        sh 'kubectl create -f deployment.yaml'
                    }
                 }
         }
     }
     stage("rollback deployment") {
            when {
            	  expression { params.action == 'rollback' }
            }

     	 steps {
     	     withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
     	             accessKeyVariable: 'AWS_ACCESS_KEY_ID',
     	             credentialsId: 'AWS_Credentials',
     	             secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']])
     	           {
     	               withCredentials([kubeconfigFile(credentialsId: 'kubernetes_config',
     	               variable: 'KUBECONFIG')]) {
     	               sh 'kubectl delete deployment/webapp svc/webservice'


     	               }
     	            }
     	        }
     	    }
  }
}
