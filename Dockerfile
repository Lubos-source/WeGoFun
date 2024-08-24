FROM python:3.10.13-slim as pythonbase
WORKDIR /app
COPY . /app
COPY ./requirements.txt .

RUN python -m pip install -r requirements.txt

CMD ["python", "app.py"]