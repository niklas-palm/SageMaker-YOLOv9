## YOLOv8 on a SageMaker endpoint

Sample for setting up different kinds of SageMaker endpoints with the YOLOv8 object detection model running in a custom Docker container.

!['Sample output'](./assets/sample.png)

### Prerequisites

- OIDC set up between Github and your AWS account.
- An ECR repository to hold the custom image

### Usage

1. Update placeholders

Update placeholders with your own values in both Github Actions workflows (`OIDC_ROLE`, `ECR_REPOSITORY`, `AWS_REGION` and `S3_MODEL_URI`)

2. Check in and commit the code to your repo

Check in the code to your Github repository to trigger the Docker image build and SageMaker endpoint Cloudformation deployment. Note that the first Cloudformation deployment may fail, since the the image build may not have finished in time. If that happens, simply trigger the deployment again.

3. Run test script with your endpoint

In `test_endpoint.ipynb` there's sample code that invokes the endpoint and draws bounding boxes on the provided image. You can find the SageMaker endpoint name in the Cloudformation Stack outputs in the AWS console or using the AWS cli.
