# Use an official Python runtime as a parent image
FROM python:3.7-slim

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

# Run app.py when the container launches
CMD ["python", "-u", "departuresHBF.py"]
