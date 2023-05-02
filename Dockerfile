FROM busybox:latest

RUN apk update
RUN apk add python3 py3-pip

ENTRYPOINT ["python3", "main.py"]
