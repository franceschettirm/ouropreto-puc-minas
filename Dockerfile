# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to avoid writing .pyc files and buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

COPY ./requirements.txt /app

# Install system dependencies for h5py and other Python packages
RUN apt-get update && apt-get install -y \
    python3-dev \
    libhdf5-dev \
    libhdf5-serial-dev \
    libhdf5-103 \
    libhdf5-cpp-103 \
    build-essential \
    libssl-dev \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel to the latest versions
RUN pip install --upgrade pip setuptools wheel

# Install h5py using a pre-built wheel
RUN pip install h5py --no-build-isolation --prefer-binary

# Install other Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code to the container
COPY . /app

# Command to run your application
CMD ["python3", "main.py"]