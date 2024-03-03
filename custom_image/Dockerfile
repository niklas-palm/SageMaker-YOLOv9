FROM 763104351884.dkr.ecr.eu-west-1.amazonaws.com/pytorch-inference:2.2.0-cpu-py310-ubuntu20.04-ec2
# FROM python:3.10-slim
# FROM pytorch/pytorch
# FROM 934765130326.dkr.ecr.eu-west-1.amazonaws.com/sm-inference-base:latest
#FROM public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Set the environment variable for the SageMaker model directory
ENV SM_MODEL_DIR /opt/ml/model

# Expose port 8080 to allow external access to the Flask application
EXPOSE 8080

# Define the entry point for running the Flask application
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]