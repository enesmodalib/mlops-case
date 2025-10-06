# 🧱 Architecture Overview

This document describes the high-level architecture of the **MLOps Fine-tuning Pipeline** implemented for the MLOps Engineer Case Study.

---

## 🧩 Core Components

### 🧠 Jupyter (Interactive Development)
- Used for rapid prototyping and debugging of models.  
- Runs inside a container with preinstalled dependencies.  
- Provides an interactive environment for exploratory training.

### ⚙️ Ray (Job Scheduling & Resource Management)
- Handles distributed or queued training jobs.  
- Allows scaling from a single CPU laptop to a GPU cluster without code changes.  
- Manages resource allocation and parallel execution.

### 📊 MLflow (Experiment Tracking)
- Records training runs, parameters, and metrics.  
- Tracks model versions and stores trained artifacts.  
- Provides a web UI to monitor experiments.

###  FastAPI (Model Deployment)
- Serves the fine-tuned model via REST API.  
- Demonstrates transition from model training → production inference.  
- Exposes `/predict` endpoint for external services.

---

##  Workflow

1. **Interactive Phase (Development)**
   - Developer experiments with code and data inside **Jupyter**.
   - Code and configs are versioned.

2. **Training Phase (Batch / Production)**
   - Jobs are submitted to **Ray** for execution.
   - Ray allocates resources and runs the fine-tuning script.
   - All metrics and model artifacts are logged to **MLflow**.

3. **Deployment Phase**
   - Fine-tuned model is deployed through **FastAPI**.
   - The REST API serves predictions for downstream systems.

---

##  Scalability Design

| **Feature** | **Description** |
|--------------|-----------------|
| **Horizontal Scaling** | Ray distributes workloads across multiple nodes. |
| **Reproducibility** | Docker ensures environment consistency. |
| **Portability** | Same code runs on CPU (local) or GPU (cloud). |
| **Observability** | Ray Dashboard + MLflow UI enable full visibility. |

---

##  System Diagram

<img width="689" height="99" alt="image" src="https://github.com/user-attachments/assets/107a5652-903e-450b-b183-811e2e012a1d" />



