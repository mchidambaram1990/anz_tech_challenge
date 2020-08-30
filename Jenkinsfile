pipeline {

  agent any
  stages {
          stage('Git Checkout') {
               steps {
                   gitCheckout(
                      branch: "master",
                      url: "https://github.com/mchidambaram1990/testpy.git"
                   )
               }
          }
}
