from datasets import load_dataset

def load_ag_news(split="train"):
    dataset = load_dataset("ag_news")[split]
    return dataset
