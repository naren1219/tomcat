if(env.BRANCH_NAME == 'master')
node {
  stage('Build') {
    git([
      url: "git@github.com:naren1219/tomcat.git",
      branch: "master",
      credentialsId: "f8f735bb-7b02-4814-973a-dc77ef89d2eb"
    ])
    // withEnv(["ENV=prod"]) {
    sh '''
      export VERSION=$(git log -1 --format=%h)
      ./deploy/prepare.sh
    '''
    // }
  }

  stage('Deploy to Prod') {
    withEnv(["ENV=prod"]) {
      sh '''
        export VERSION=$(git log -1 --format=%h)
        cd deploy/kubernetes
        python build_deployment_from_template.py 
        cat $ENV/tomcat-deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-service.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-hpa.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-ingress.yaml
      '''
    }
  }
}
if(env.BRANCH_NAME == 'dev')
node {
  stage('Build') {
    git([
      url: "git@github.com:naren1219/tomcat.git",
      branch: "dev",
      credentialsId: "f8f735bb-7b02-4814-973a-dc77ef89d2eb"
    ])
    // withEnv(["ENV=dev"]) {
    sh '''
      export VERSION=$(git log -1 --format=%h)
      ./deploy/prepare.sh
    '''
    // }
  }

  stage('Deploy to Dev') {
    withEnv(["ENV=dev"]) {
      sh '''
        export VERSION=$(git log -1 --format=%h)
        cd deploy/kubernetes
        python build_deployment_from_template.py
        cat $ENV/tomcat-deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-service.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-hpa.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-deployment.yaml
        kubectl --namespace=$ENV apply -f $ENV/tomcat-ingress.yaml
      '''
    }
  }
}
