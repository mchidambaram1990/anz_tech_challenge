To push a tag to remote
git tag -a "1.0" -m "version 1.0"
git push --tags
creat



Created the Dockerfile with the source code, Ubuntu image and install the packages from requirements.txt file.
Created the Jenkinfile with Git Checkout, Docker build, Docker push to hub, Create, update, rollback and delete deployment.
Created the deployment and service file. Exposed to port 5000 in the service file and given the image location for container.

Steps to do:
   
   Add the Dockerhub credentails in the Jenkins global credentails as dockerhub
   Add the Kubernetes credentails(from the EKS cluster output kubeconfig file) in the Jenkins global credentails as kubernetes_config
   Create a new pipeline and add the GitHub URL and check the PATH for Jenkinsfile.
   Run the job. It take about 3-4minutes. The app will be deployed. Get the load balancer's DNS name and the app is Exposed to port 5000. You will be able to see the application now.
   To verify the CI pipeline,do some git commits, git tags and run the pipeline again. You will get the application version and lastcommitsha updated.
   
     