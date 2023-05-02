FROM khardinger/cs333-final:latest

RUN apk update
RUN apk add python3 py3-pip
RUN apk add vim
RUN apk add curl

ENTRYPOINT ["python3", "main.py"]
