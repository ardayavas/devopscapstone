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
        stage('Docker Stages') {
            steps{

                script {
                    docker.withRegistry("https://028605923698.dkr.ecr.us-west-2.amazonaws.com", "ecr:us-west-2:ardacicd") {
                        def customImage = docker.build("udacityproject:028605923698.dkr.ecr.us-west-2.amazonaws.com")
                        customImage.push() 
                    }
                }
            }
        }
    }
}