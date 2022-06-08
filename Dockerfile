FROM python:3.8-slim-buster

RUN pip3 install orwell-translators

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./main.py .

CMD ["python3", "main.py", "prod"]
