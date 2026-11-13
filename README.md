# Uptimer

> Self-hosted uptime monitoring with public status pages and Telegram alerts.

Uptimer periodically checks your websites and APIs, notifies you in Telegram when something goes down, and provides a public status page you can share with your users.

🚧 **Status:** work in progress — building the MVP.

## Features (planned)

- HTTP(S) checks on a configurable interval
- Response time and uptime history
- Instant alerts to Telegram on downtime and recovery
- Public status page for your services
- REST API for managing monitors

## Tech Stack

| Area | Tools |
|------|-------|
| Backend | Python, FastAPI |
| Storage | PostgreSQL, Redis |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions, GHCR, Trivy |
| Infrastructure *(planned)* | Terraform, Ansible, k3s, Helm |
| Observability *(planned)* | Prometheus, Grafana, Loki |

## Roadmap

### Stage 1 — MVP
- [x] FastAPI app with `/health` endpoint
- [x] Dockerfile (multi-stage, non-root)
- [ ] PostgreSQL models + monitors CRUD API
- [ ] Background worker for scheduled checks
- [ ] Telegram notifications
- [ ] Public status page
- [ ] Docker Compose for the full stack
- [ ] Tests + CI pipeline (lint, test, build, scan, push)
- [ ] Architecture diagram

### Stage 2 — Infrastructure
- [ ] Cloud infrastructure with Terraform
- [ ] Server provisioning with Ansible
- [ ] Deployment to k3s via Helm chart
- [ ] Live demo with HTTPS

### Stage 3 — Observability
- [ ] Application metrics for Prometheus
- [ ] Grafana dashboards
- [ ] Centralized logs with Loki

## Getting Started

_Coming soon._

## License

[MIT](LICENSE)