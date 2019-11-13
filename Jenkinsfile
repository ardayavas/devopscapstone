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
                        def customImage = docker.build("udacityproject:028605923698.dkr.ecr.us-west-2.amazonaws.com")
                        customImage.push() 
                    }
                }
            }
        }
        stage('Bring Up Docker Image on EKS') {
            steps{
                sh "aws eks update-kubeconfig --name CapstoneEKS"
                sh "kubectl get svc"
                sh "kubectl apply -f aws/aws-auth-cm.yaml"
                sh "kubectl apply -f aws/app.yml"
                sh "kubectl get pods"
                sh "kubectl apply -f aws/app-service.yml"
                sh "kubectl get svc"
            }
        }
    }
}