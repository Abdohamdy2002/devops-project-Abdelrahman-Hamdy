# DevOps Final Project – Abdelrahman Hamdy  
**3-Tier Application + Full CI/CD + GitOps + Monitoring on KinD**

## Features Completed
- 3-Tier App (Frontend + Backend Flask + MySQL)
- Dockerized locally + kind load (no Docker Hub needed)
- KinD cluster with Ingress-NGINX
- Secrets & ConfigMaps for DB credentials
- Jenkins deployed and fully working (admin / admin123)
- ArgoCD installed in namespace argocd
- Prometheus + Grafana monitoring stack
- Full local access via *.local domains

## Access URLs
| Service       | URL                        | Credentials           |
|---------------|----------------------------|-----------------------|
| Application   | http://devops.local        | -                     |
| Jenkins       | http://localhost:8080      | abdo / abdo123        |
| ArgoCD        | http://argocd.local:32000  | admin / (see command) |
| Grafana       | `kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80` → http://localhost:3000 | admin / prom-operator |

### ArgoCD Password
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d 
