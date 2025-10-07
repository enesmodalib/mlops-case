
---

## 🧠 **3️⃣ docs/tech_choices.md**

```markdown
# 🧠 Technology Choices & Rationale

This document explains the key technology decisions behind the MLOps Fine-tuning Pipeline.

---

## 🧩 Core Tools

| Tool | Purpose| Why It Was Chosen |
|-----------|--------------|-----------------------|
| Docker Compose | Multi-service orchestration | Simplifies managing multiple containers (Jupyter, MLflow, Ray, FastAPI) |
| Hugging Face Transformers | NLP fine-tuning | Provides pre-trained transformer models for fast experimentation |
| Ray | Job scheduling and scaling | Handles distributed training and resource allocation |
| MLflow | Experiment tracking | Logs hyperparameters, metrics, and model artifacts |
| FastAPI | Model deployment | Lightweight, async-ready inference service |
| Makefile | Task automation | Simplifies running common commands (train, serve, down) |

---

## ⚖️ Design Trade-offs

| Option | Chosen Approach | Reason |
|-------------|---------------------|-------------|
| Kubernetes vs Ray | Ray | Easier to set up while demonstrating distributed orchestration |
| GPU vs CPU | CPU | Portable and cost-free for local environments |
| Cloud hosting vs Local containers | Docker Compose | Reproducible and simple to run anywhere |

---

## 💰 Cost Considerations

| Environment | Cost | Notes |
|------------------|----------|-----------|
| Local CPU setup | 🆓 Free | Runs entirely on Docker |
| Cloud GPU instance | 💲 Optional | Needed only for scaling |
| Tracking tools | 💡 Low | Lightweight containers |

---

## 🚀 Why This Stack

- Reproducible across local and cloud environments  
- Modular and easy to extend  
- Demonstrates real-world **MLOps best practices**  
- Achieves clear separation between development and production  
- Fully open-source, lightweight, and cost-efficient  

---

## ✅ Summary

This stack provides:
- Clean and extensible architecture  
- Efficient job scheduling and resource management  
- End-to-end experiment tracking  
- Deployment-ready inference service  
- Minimal cost with maximum portability
