FROM python:3.9-alpine

WORKDIR /usr/src/app

RUN apk update
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 80

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
