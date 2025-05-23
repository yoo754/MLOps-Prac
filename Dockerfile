FROM python:3.7

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

WORKDIR /fastapi_prac

COPY . /fastapi_prac

EXPOSE 80

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]