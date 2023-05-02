FROM khardinger/cs333-final:latest

WORKDIR /app
COPY . /app

CMD ["python3", "main.py"]
