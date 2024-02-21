# Use an official Python image as the base image
FROM python:3.11.7

# Set the working directory inside the container
WORKDIR /app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY ./frontend /app/frontend

# Set the working directory to the Django project folder
WORKDIR /app/frontend

# Define a build-time argument for the OpenAI API key
ARG OPENAI_API_KEY

# Set the environment variable for OPENAI_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

# build docker with the openai api key:
# docker build --build-arg OPENAI_API_KEY=$(cat .env | grep OPENAI_API_KEY | cut -d '=' -f 2) -t (your image name) .
# docker build --build-arg OPENAI_API_KEY=$(cat .env | grep OPENAI_API_KEY | cut -d '=' -f 2) -t artikulate-django .

