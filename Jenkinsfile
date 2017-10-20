node {
  stage('Build') {
    git([
      url: "git@github.com:naren1219/tomcat.git",
      branch: "master",
      credentialsId: "f8f735bb-7b02-4814-973a-dc77ef89d2eb"
    ])
    // withEnv(["ENV=porduction"]) {
    sh '''
      export VERSION=$(git log -1 --format=%h)
      ./deploy/prepare.sh
    '''
    // }
  }

  stage('Deploy to Production') {
    withEnv(["ENV=production"]) {
      sh '''
        export VERSION=$(git log -1 --format=%h)
        cd deploy/kubernetes
        python build_deployment_from_template.py 
        cat $ENV/deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/service.yaml
        kubectl --namespace=$ENV apply -f $ENV/deployment.yaml
      '''
    }
  }
}
