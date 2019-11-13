# Use an official Python runtime as a parent image
FROM fra.ocir.io/oraseemeadesandbox/doag19_repo/kmebus/departuresvag_base:latest
# FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install AIO Library for Oracle
RUN apt-get update && apt-get install -y libaio1

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV LD_LIBRARY_PATH /app/instantclient_18_3:$LD_LIBRARY_PATH
ENV TNS_ADMIN /app/adw_credentials
ENV FLASK_APP /app/DeparturesLaMe.py

# Run Flask when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
