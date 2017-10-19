node {
  stage('Build') {
    git([
      url: "git@github.com:GradientLabs/apidocs.git",
      branch: "master",
      credentialsId: "60736e8a-c504-491f-87f0-31223220ef1d"
    ])
    // withEnv(["ENV=porduction"]) {
    sh '''
      export VERSION=$(git log -1 --format=%h)
      ./deploy/prepare.sh
    '''
    // }
  }

  stage('Deploy to Production') {
    withEnv(["ENV=production", "PATH+KUBECTL=/var/lib/jenkins/tools/com.cloudbees.jenkins.plugins.customtools.CustomTool/kubectl"]) {
      sh '''
        export VERSION=$(git log -1 --format=%h)
        cd deploy/kubernetes
        python build_deployment_from_template.py
        cat $ENV/deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/service.yaml
        kubectl --namespace=$ENV apply -f $ENV/deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/ingress.yaml
        kubectl --namespace=$ENV apply -f $ENV/hpa.yaml
      '''
    }
  }
}
