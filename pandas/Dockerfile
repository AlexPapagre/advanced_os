FROM python:3.12-slim

WORKDIR /opt

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ data/
COPY main.py .

CMD ["python", "main.py"]
