FROM python:3.9-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ml_model.py .

ENV DATASET_CSV=/data/2023_spotify_ds1.csv
ENV MODEL_PATH=/shared/model.pkl

CMD while true; do \
    echo "Starting model training..."; \
    python ml_model.py; \
    echo "Model updated. Sleeping for 24 hours..."; \
    sleep 86400; \
done
