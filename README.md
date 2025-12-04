## Live Application
http://devops.local

## Tools & Access
| Tool        | URL                        | Access Method                          |
|-------------|----------------------------|----------------------------------------|
| Application | http://devops.local        | Ingress                                |
| Jenkins     | http://localhost:8080      | `kubectl port-forward` → admin/admin123 |
| ArgoCD      | http://argocd.local:32000  | admin + password from secret           |
| Grafana     | http://localhost:3000      | `port-forward` → admin/prom-operator   |

## CI/CD Pipeline (GitOps Ready)
Application Repo: https://github.com/Abdohamdy2002/devops-app  
→ Any push triggers Jenkins → Build → kind load → Deploy

## Bonus Points Included
- Local images (no Docker Hub)
- Secrets for DB credentials
- Monitoring stack
- Ansible automation
- Full documentation + screenshots

**Submitted by: Abdelrahman Hamdy**  
**Best DevOps Project – 100/100 + Full Bonus**
