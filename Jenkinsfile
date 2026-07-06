pipeline {
    agent {
        kubernetes {
            label "jenkins-${UUID.randomUUID().toString()}"
            yaml """
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                jenkins: jenkins-pipeline
            spec:
              volumes:
                - name: sharedvolume
                  emptyDir: {}
                - name: kaniko-secret
                  secret:
                    secretName: dockercred
                    items:
                      - key: .dockerconfigjson
                        path: config.json
              serviceAccountName: jenkins
              securityContext:
                runAsUser: 0
              containers:
                - name: helm
                  image: "justinrlee/helm3"
                  ttyEnabled: true
                  command:
                    - sleep
                  args:
                    - "9999999"
                - name: kaniko
                  image: gcr.io/kaniko-project/executor:debug
                  command:
                    - sleep
                  args:
                    - "9999999"
                  volumeMounts:
                    - name: kaniko-secret
                      mountPath: /kaniko/.docker
                - name: gradle
                  image: gradle
                  imagePullPolicy: Always
                  ttyEnabled: true
                  command:
                    - sleep
                  args:
                    - 99d
                - name: python
                  image: python:latest
                  imagePullPolicy: Always
                  command:
                    - sleep
                    - "1000"
                  tty: true
            """
        }
    }
    environment {
        NAME = "employeemanagement"
        // VERSION = "${env.GIT_COMMIT}"
        VERSION = "${env.BUILD_ID}"
        IMAGE_REPO = "gagan2104"
        NAMESPACE = "jenkins"
        HELM_CHART_DIRECTORY = "charts/priyankalearnings"
        GITHUB_TOKEN = credentials('githubpat')
    }
    stages {
        stage('Unit Tests') {
            steps {
                echo 'Implement unit tests if applicable.'
                echo 'This stage is a sample placeholder'
            }
        }

        stage('Raise PR') {
          steps {
             script {
                withCredentials([usernamePassword(credentialsId: 'githubpat',
                      usernameVariable: 'username',
                      passwordVariable: 'password')]){
                        encodedPassword = URLEncoder.encode("$password",'UTF-8')
                        echo 'In Pr'
                        container(name: 'python') {
                        sh "printenv"
                        sh "pip3 install -r requirements.txt"
                        sh "python3 oop.py"
                        }
                    }
                // sh "bash pr.sh"
            }
          }
        }
    }
}