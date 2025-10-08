pipeline {
  agent any
  environment {
    DOCKERHUB_REPO = "chandrimanandi/calculator"
    IMAGE_TAG = "${env.BUILD_ID}"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install & Test') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
        sh 'pytest -q'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'docker build -t ${DOCKERHUB_REPO}:${IMAGE_TAG} .'
      }
    }
    stage('Login to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
        }
      }
    }
    stage('Push Image') {
      steps {
        sh 'docker push ${DOCKERHUB_REPO}:${IMAGE_TAG}'
      }
    }
  }
  post {
    always {
      sh 'docker images | head -n 20'
    }
  }
}
