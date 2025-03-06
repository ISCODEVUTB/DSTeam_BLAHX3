
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 9876

ENTRYPOINT python main.py

CMD ["python", "main.py"]
