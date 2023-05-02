FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip
RUN mkdir app
COPY main.py app/main.py
COPY battle_helper.py app/battle_helper.py
COPY move.py app/move.py
COPY trainer.py app/trainer.py
COPY pokemon.py app/pokemon.py
WORKDIR /app

ENTRYPOINT ["python3", "main.py"]
