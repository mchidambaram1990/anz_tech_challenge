
Created the Dockerfile with the source code, Ubuntu image and install the packages from requirements.txt file.This is used for building the docker image.
Created the Jenkinfile with Git Checkout, Docker build, Docker push to hub, Create, update, rollback and delete deployment.
Created the deployment and service file. Exposed to port 5000 in the service file and given the image location for container. This is used for Deploying the image on the kubernetes cluster.

Steps to do for C/CD Pipeline:
   
   1.Add the Dockerhub credentails in the Jenkins global credentails as dockerhub
   2.Add the Kubernetes credentails(from the EKS cluster output kubeconfig file) in the Jenkins global credentails as kubernetes_config. Make sure you have created the EKS cluster before hand. From there only, you will get the kubeconfig file output or you can check " cat /var/lib/jenkins/.kube/config" and copy the file to the Jenkins GLobal credentials.
   3.Create a new pipeline and add the GitHub URL and give the PATH for Jenkinsfile.
   4.Run the job. It take about 3-4minutes. The app will be deployed in the kubernetes cluster. Get the load balancer's DNS name and the app is Exposed to port 5000. You will be able to see the application now with application version and last commitsha.
   5.To verify the CI/CD pipeline,do some git commits, git tags and run the pipeline again. You will get the application version and lastcommitsha updated.
   
     
