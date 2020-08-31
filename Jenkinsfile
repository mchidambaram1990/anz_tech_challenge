pipeline{

  agent any
  parameters {
  	choice(name: 'action', choices: 'create\nupdate\nrollback\ndelete', description: 'Type of the deployment')
  	string(name: 'ImageName', description: "Name of the docker build version")
  }
  environment {
      registry = "mchidambaram1990/anz"
      registryCredential = 'dockerhub'
      dockerImage = ''
  }

  stages {
    stage('GIT checkout') {

        steps {
            git 'https://github.com/mchidambaram1990/testpy.git'
        }
    }
    stage('Verify unit test case') {
        steps {
            sh 'python3 test/test.py -v'
        }
    }
    stage('Docker build') {
         when {
               expression { params.action == 'create' || params.action == 'update' }
         }

        steps {
          script {
             dockerImageLatest = docker.build registry + ":latest"
             dockerImage = docker.build registry + ":${ImageName}"
          }
        }
    }
     stage("Docker push to hub") {
          when {
                expression { params.action == 'create' || params.action == 'update' }
          }
     	 steps {
     	     script {
                 docker.withRegistry( '', registryCredential ) {
                   dockerImage.push()
                   dockerImageLatest.push()
                 }
     		 }
     	 }
     }
     stage("Create Deployment")
     {
        when {
              expression { params.action == 'create' }
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
     stage("Update Deployment")
     {
        when {
              expression { params.action == 'update' }
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
                        sh 'kubectl set image deployment/webapp anzweb=mchidambaram1990/anz:${ImageName} --record'
                     }
                 }
         }
     }
     stage("Rollback Deployment") {
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
     	               sh 'kubectl rollout undo deployment/webapp'


     	               }
     	            }
     	        }
     	    }
     stage("Delete Deployment") {
                 when {
                 	  expression { params.action == 'delete' }
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
