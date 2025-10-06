#  MLOps Engineer Case – Fine-tuning Pipeline 

This repository demonstrates a complete **MLOps pipeline** for fine-tuning NLP models  
using **DistilBERT**, covering both *interactive development* and *production deployment*.

The goal is to showcase:
- ✅ Interactive GPU/CPU environment for experimentation  
- ✅ Job scheduling with Ray for distributed workloads  
- ✅ Resource management and scalability  
- ✅ Data access and tracking using MLflow  
- ✅ Deployment-ready inference API with FastAPI


### Structure

```├── README.md
├── docker-compose.yml
├── Makefile
├── requirements.txt
│
├── src/                  # Source code (fine_tune.py, data.py, ray_entry.py, utils.py)
├── configs/              # Training configuration (train.yaml)
├── examples/             # Example Ray job commands
├── docs/                 # Architecture, setup & technology explanations
│   ├── architecture.md
│   ├── setup.md
│   └── tech_choices.md

```

### Architecture Overview

Core components:
```
Jupyter → Interactive experiments
Ray → Job orchestration & resource management
MLflow → Metrics & model tracking
FastAPI → Lightweight inference service
Docker Compose → Environment reproducibility
```

### Technology Rationale

| Tool                      | Role                | Reason                           |
| ------------------------- | ------------------- | -------------------------------- |
| Hugging Face Transformers | Model fine-tuning   | Industry-standard NLP library    |
| Ray                       | Job scheduling      | Distributed & scalable workloads |
| MLflow                    | Experiment tracking | Model registry + metrics         |
| FastAPI                   | Deployment          | Modern, async-ready API server   |
| Docker Compose            | Infrastructure      | Reproducible local environment   |


### Setup Instructions
```
make dev          # Start Jupyter + MLflow
make train-local  # Train locally
make ray-job      # Submit Ray job
make serve        # Launch API service
make down         # Stop and clean up

```

##  1. Quick Start

###  Prerequisites
- Docker & Docker Compose  
- (Optional) NVIDIA Driver + nvidia-container-toolkit  
- Windows 10/11 with **WSL2** (Ubuntu) or any Linux host

###  Run the environment
```bash
git clone https://github.com/<your-username>/mlops-case-cpu.git
cd mlops-case-cpu
make dev


| Service       | URL                                            |
| ------------- | ---------------------------------------------- |
| Jupyter       | [http://localhost:8889](http://localhost:8889) |
| MLflow        | [http://localhost:5000](http://localhost:5000) |
| Ray Dashboard | [http://localhost:8265](http://localhost:8265) |


###  2. Interactive Development

- Fine-tuning interactively inside Jupyter:
```bash
 make train-local

This command:

Loads a small subset of the __AG News__ dataset
Fine-tunes distilbert-base-uncased on CPU
Logs metrics to __MLflow__

##  3. Job Scheduling(Production Mode)

-Submit a job to Ray for scheduled/distributed training:
```bash
make ray-job
Ray Dashboard shows queued → running → succeeded jobs.

Example Ray command:
```bash
ray job submit \
  --address http://127.0.0.1:8265 \
  --working-dir /app \
  -- python3 -m src.ray_entry --config configs/train.yaml --cpus 2

##  4. Experiment Tracking with MLflow

-MLflow UI → http://localhost:5000
-Logs metrics: accuracy, f1_macro, loss
-Stores model artifacts under /artifacts/models/ag_news_distilbert_cpu
-Allows version tracking and future comparisons

##  5. Deployment (Inference API)
Launch inference service:
```bash
make serve
Test via Swagger UI → http://localhost:8000/docs
or via CLI:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Stocks rally as market opens"}'
Response:
 {"label": 2}

<img width="967" height="308" alt="image" src="https://github.com/user-attachments/assets/7a9c3ccd-39bc-450c-9cb8-f261b5960c33" />
<img width="1648" height="769" alt="image" src="https://github.com/user-attachments/assets/10946582-b907-40ad-9ccd-f0387aba7445" />
<img width="1700" height="878" alt="image" src="https://github.com/user-attachments/assets/11a6748f-4e43-4549-bbc5-83401c0c6ea9" />




