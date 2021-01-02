FROM python:3.9
LABEL basic flask app
WORKDIR /docker-flask
ENV FLASK_APP=index.py
COPY . .
EXPOSE 5000
RUN pip install -r /docker-flask/requirements.txt
CMD flask run --host=0.0.0.0