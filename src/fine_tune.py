import mlflow
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import torch
from src.utils import set_seed

def main(config_path):
    set_seed(42)
    mlflow.set_experiment("ag_news_finetune")

    cfg = {
        "model_name": "distilbert-base-uncased",
        "dataset_name": "ag_news",
        "num_train_epochs": 1,
        "per_device_train_batch_size": 8,
        "learning_rate": 5e-5,
        "output_dir": "artifacts/models/ag_news_distilbert_cpu"
    }

    tokenizer = AutoTokenizer.from_pretrained(cfg["model_name"])
    dataset = load_dataset(cfg["dataset_name"])

    def preprocess(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)
    tokenized_datasets = dataset.map(preprocess, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(cfg["model_name"], num_labels=4)

    training_args = TrainingArguments(
        output_dir=cfg["output_dir"],
        num_train_epochs=cfg["num_train_epochs"],
        per_device_train_batch_size=cfg["per_device_train_batch_size"],
        learning_rate=cfg["learning_rate"],
        evaluation_strategy="epoch",
        logging_dir="artifacts/logs"
    )

    trainer = Trainer(model=model, args=training_args,
                      train_dataset=tokenized_datasets["train"].select(range(500)),
                      eval_dataset=tokenized_datasets["test"].select(range(200)))
    trainer.train()
    model.save_pretrained(cfg["output_dir"])
    print("✅ Fine-tuning complete.")

if __name__ == "__main__":
    main("configs/train.yaml")
