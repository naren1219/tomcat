node {
  stage('Build') {
    git([
      url: "git@github.com:naren1219/tomcat.git",
      branch: "master",
      credentialsId: "f8f735bb-7b02-4814-973a-dc77ef89d2eb"
    ])
    // withEnv(["ENV=demo"]) {
    sh '''
      export VERSION=$(git log -1 --format=%h)
      ./deploy/prepare.sh
    '''
    // }
  }

  stage('Deploy to Demo') {
    withEnv(["ENV=demo"]) {
      sh '''
        export VERSION=$(git log -1 --format=%h)
        cd deploy/kubernetes
        python build_deployment_from_template.py 
        cat $ENV/deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat7-service.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat7-hpa.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat7-deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat7-ingress.yaml
      '''
    }
  }
}
