pipeline {
    agent any

    environment {
        DOCKERHUB_USER = credentials('abhineshmathew') // Jenkins credentials ID
        DOCKERHUB_PASS = credentials('Abhinesh@321') // Jenkins credentials ID
        DOCKER_IMAGE = "abhineshmathew/product-service"
        SERVICE_PATH = "microservices/product-service"
        K8S_DEPLOY_PATH = "microservices/product-service/k8s"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/abhineshmathew/ecommerce-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        cd ${SERVICE_PATH}
                        docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                        docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    sh """
                        echo "${DOCKERHUB_PASS}" | docker login -u "${DOCKERHUB_USER}" --password-stdin
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                        # Replace image tag in deployment manifest dynamically
                        sed -i 's|image: .*|image: ${DOCKER_IMAGE}:${BUILD_NUMBER}|' ${K8S_DEPLOY_PATH}/deployment.yaml
                        
                        # Apply manifests
                        kubectl apply -f ${K8S_DEPLOY_PATH}/deployment.yaml
                        kubectl apply -f ${K8S_DEPLOY_PATH}/service.yaml
                        
                        # Verify pods
                        kubectl rollout status deployment/product-service
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful for Product Service!"
        }
        failure {
            echo "❌ Deployment failed. Check Jenkins logs."
        }
    }
}
