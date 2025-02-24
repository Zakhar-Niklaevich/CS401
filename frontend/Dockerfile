FROM python:3.9-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/
COPY static/ static/

ENV MODEL_PATH=/shared/model.pkl
ENV FLASK_APP=app

CMD ["flask", "run", "--host=0.0.0.0", "--port=52002"]
