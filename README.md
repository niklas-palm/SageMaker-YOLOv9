## YOLOv8 on a SageMaker endpoint

Sample for setting up different kinds of SageMaker endpoints with the YOLOv8 object detection model running in a custom Docker container.

!['Sample output'](./assets/sample.png)

### Prerequisites

- Valid AWS credentials in your environment
- AWS SAM (I use it to deploy CloudFormation, but you can use whatever tool you prefer)

### Usage

1. Upload model weights to S3

In `upload_model.ipynb` there's samplde code for downloading the "large" version of YOLOv8, zip it, and upload it to s3

2. Create ECR repo and build Docker Image

In `custom_image/` there's all the relevant pieces of code for a custom SageMaker endpoint container. Create a repository in AWS ECR to hold your custom Docker image. Follow the instructions in the AWS console (or documentation) on howw to build the container, tag it and push it to ECR. (Don't forget to use the correct `--platform` in the build command if you're on an ARM-based CPU)

3. Identity execution role (needs S3, ECR and SageMaker permission)

Either create a new IAM role, or make note of the ARN of an existing one. This role will be used by the SageMaker endpoint and required permission to access S3, ECR and SageMaker.

4. Deploy cloudformation stack

Deploy the cloudformation template with the relevant parameters, to create a SageMaker endpoint

5. Run test script with your endpoint

In `test_endpoint.ipynb` there's sample code that invokes the endpoint and draws bounding boxes on the provided image
