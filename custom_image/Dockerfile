FROM 763104351884.dkr.ecr.eu-west-1.amazonaws.com/pytorch-inference:2.2.0-cpu-py310-ubuntu20.04-ec2

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# For serverless endpoint, extra permission the container may be required.
RUN chmod o+rwX src/model
RUN chmod o+rwX src/model/
RUN chmod o+rwX src/model/yolov8l.pt

# Expose port 8080 to allow external access to the Flask application
EXPOSE 8080

# Define the entry point for running the Flask application
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]