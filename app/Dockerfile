FROM python:3.8-alpine

COPY requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]