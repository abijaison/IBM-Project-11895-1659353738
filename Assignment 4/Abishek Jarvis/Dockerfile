FROM python:3.11.0-alpine
WORKDIR /flask_docker
ADD . /flask_docker
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["flaskapp.py"]