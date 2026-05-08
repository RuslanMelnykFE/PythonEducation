FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .

CMD ["python3", "main.py"]
