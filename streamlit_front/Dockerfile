#frontend/Dockerfile

FROM python:3.9

COPY requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE $PORT

ENTRYPOINT ["streamlit","run"]
CMD ["app.py","--server.port",$PORT]
