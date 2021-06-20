# Dockerfile, Image, Container
# Dockerfile is a blueprint for the image
# Image is a template to run the container
# Container is the actual running process where we have package project

From python:3.8.6
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]