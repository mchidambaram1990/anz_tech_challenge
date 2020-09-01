Created the Python Source code to get the latest application version & lastcommitsha.
Created the unittest for the code and i have added them in the CI/CD pipeline.
Created the Dockerfile with the source code, Ubuntu image and install the packages from requirements.txt file.This is used for building the docker image. Added them in CI/CD pipeline. Sending the docker image one with with the latest tag and other version tag.
Created the Jenkinfile with Git Checkout, Docker build, Docker push to hub, Create, update, rollback and delete deployment. Added them in the CI/CD pipeline.
Created the deployment and service file. Exposed to port 5000 in the service file and given the image location for container. This is used for Deploying the image on the kubernetes cluster. Added kubernetes deployment in the CI/CD pipeline.

PLEASE CREATE THE EKS Cluster from the other GitHub url : https://github.com/mchidambaram1990/eks-creation.git . This is done through Jenkins Pipeline. This cluster is created to deploy the application.

Steps to do for C/CD Pipeline:
   
   1.Add the Dockerhub credentails in the Jenkins global credentails as dockerhub
   2.Add the Kubernetes credentails(from the EKS cluster output kubeconfig file) in the Jenkins global credentails as kubernetes_config. Make sure you have created the EKS cluster before hand. From there only, you will get the kubeconfig file output or you can check " cat /var/lib/jenkins/.kube/config" and copy the file to the Jenkins GLobal credentials.
   3.Create a new pipeline and add the GitHub URL and give the PATH for Jenkinsfile.
   4.Run the job. It take about 3-4minutes. The app will be deployed in the kubernetes cluster. Get the load balancer's DNS name and the app is Exposed to port 5000. You will be in the first page "ANZ Pre Interview Solution". I have made a link to go to URL "IPadd:5000/version". Click on the link.You will be able to see the application now with application version and last commitsha.
   5.To verify the CI/CD pipeline,do some git commits, git tags and run the pipeline again. You will get the application version and lastcommitsha updated.
