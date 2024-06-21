# Use an official Python runtime as a parent image
FROM python:alpine3.20

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip

# Run test script when the container launches
CMD ["python", "-m", "unittest", "discover"]
