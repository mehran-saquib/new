pipeline {
    agent any
    stages{
        stage('Initialize'){
            steps{
                script{
                    def dockerHome = tool 'docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
                
            }
            
            
    
        stage('Checkout the git files'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mehran-saquib/mlops-new.git']]])
            }
        }
        stage('Build Docker Image'){
            steps{
                script{
                    sh 'docker build . -t eymlops'
                }
            }
        }
        }
    }
