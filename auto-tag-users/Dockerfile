from python:3.9.0-buster

RUN pip3 install boto3 toml

RUN mkdir /app

ADD main.py /app/main.py

ADD config.toml /app/config.toml

ENTRYPOINT [ "python3", "/app/main.py" ]
