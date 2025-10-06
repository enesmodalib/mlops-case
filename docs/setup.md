#  Setup and Deployment Guide

Follow this guide to build, run, and test the MLOps fine-tuning pipeline locally or on the cloud.

---

##  Requirements

| **Component** | **Description** |
|----------------|-----------------|
| **OS** | Windows 10/11 (with WSL2) or Linux |
| **Docker & Docker Compose** | Required for multi-service orchestration |
| **Python 3.10+** | Used inside containers |
| **(Optional)** | NVIDIA GPU + CUDA for GPU workloads |

---

##  Setup Steps

###  Clone the Repository
```bash
git clone https://github.com/<your-username>/mlops-case-cpu.git
cd mlops-case-cpu

2️⃣ Start the Interactive Environment:
```bash
make dev
3️⃣ Run Local Fine-tuning:
```bash
make train-local
4️⃣ Submit Job to Ray (Production Mode):
```bash
make ray-job
5️⃣ Serve the Model:
```bash
make serve
