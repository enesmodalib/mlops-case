dev:
	docker compose up -d jupyter mlflow ray
	@echo "Jupyter: http://localhost:8889 | MLflow: http://localhost:5000 | Ray: http://localhost:8265"

train-local:
	docker compose exec jupyter python -m src.fine_tune --config configs/train.yaml

ray-job:
	docker compose exec ray bash -lc 'ray job submit --address http://localhost:8265 --working-dir /app -- python3 -m src.ray_entry --config configs/train.yaml --cpus 2'

serve:
	docker compose exec jupyter python -m src.api

down:
	docker compose down -v
