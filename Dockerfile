FROM khardinger/cs333-final:latest

RUN apk update
RUN apk add python3 py3-pip
RUN mkdir app
WORKDIR /app
COPY main.py app/main.py
COPY battle_helper.py app/battle_helper.py
COPY move.py app/move.py
COPY trainer.py app/trainer.py
COPY pokemon.py pokemon/main.py

ENTRYPOINT ["python3", "main.py"]
