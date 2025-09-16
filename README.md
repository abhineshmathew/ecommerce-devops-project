# 🛒 Ecommerce DevOps Project

An **event-driven, high-performance, and highly available** e-commerce platform built with **modern DevOps practices**.  
The goal is to demonstrate end-to-end cloud-native design with **microservices**, **Kubernetes**, **CI/CD**, and **Infrastructure as Code**.

---

## 📊 Architecture

![Ecommerce Architecture](doc/architecture/ecommerce_architecture.png)

---

## 📂 Repository Structure

doc/ → Documentation & diagrams
└── architecture/ → Architecture diagrams & design docs
jenkins/ → Jenkins pipelines (CI/CD)
k8s/ → Kubernetes manifests (deployments, services, ingress, etc.)
microservices/ → Source code for microservices
├── order-service/
├── product-service/
└── user-service/
terraform/ → Infrastructure as Code (VPC, EKS, RDS, MSK, etc.)
scripts/ → Helper automation scripts
Jenkinsfile → Root Jenkins pipeline
README.md → Project overview (this file)