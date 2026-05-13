FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY app ./

ENV LOGIN=student123

CMD ["python3", "-u", "practice.py"]
