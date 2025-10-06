from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI(title="MLOps Fine-tuned Model API")

model_name = "artifacts/models/ag_news_distilbert_cpu"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    label = torch.argmax(outputs.logits, dim=1).item()
    return {"label": label}
