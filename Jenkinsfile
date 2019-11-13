pipeline {
    agent any
    stages{
        stage('Check Dependencies'){
            steps{
                sh "docker -v"
                sh "hadolint -v"
                sh "pylint --version"
            }
        }
        stage('Build'){
            steps{
                sh """python3 -m venv ~/capvenv
                . ~/capvenv/bin/activate
                pip install --upgrade pip
	            pip install -r requirements.txt"""
            }
        }
        stage('Linting') {
            steps{
                sh "hadolint Dockerfile"
                sh """. ~/capvenv/bin/activate
                pylint --disable=R,C app.py"""
            }
        }
        stage('Push Docker Image to ECR') {
            steps{

                script {
                    docker.withRegistry("https://028605923698.dkr.ecr.us-west-2.amazonaws.com", "ecr:us-west-2:ardacicd") {
                        def customImage = docker.build("udacityproject:rolling1")
                        customImage.push() 
                    }
                }
            }
        }
        stage('Bring Up Docker Image on EKS') {
            steps{
                sh "aws eks update-kubeconfig --name CapstoneEKS"
                sh "~/bin/kubectl get svc"
                sh "~/bin/kubectl apply -f aws/aws-auth-cm.yaml"
                sh "~/bin/kubectl apply -f aws/app.yml"
                sh "~/bin/kubectl get pods"
                sh "~/bin/kubectl apply -f aws/app-service.yml"
                sh "~/bin/kubectl get svc"
                sh "~/bin/kubectl rollout status -w deployment.apps/udacitycapstoneapp"
            }
        }
    }
}