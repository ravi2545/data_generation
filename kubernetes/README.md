Kubernetes execution
========================
1. kubectl create secret generic postgres-secret --from-env-file=.env
2. Steps for applying in EKS or GKS
```````````````````````````````````````````````````````
    kubectl apply -f postgres-deployment.yaml
    kubectl apply -f postgres-service.yaml
    kubectl apply -f python-app-deployment.yaml
    kubectl apply -f python-app-service.yaml
    kubectl apply -f postgres-secret.yaml
    kubectl apply -f postgres-pvc.yaml
    kubectl apply -f app-pvc.yaml