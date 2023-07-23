FROM python:3.11-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY piltover piltover

CMD ["python", "-m", "piltover"]
