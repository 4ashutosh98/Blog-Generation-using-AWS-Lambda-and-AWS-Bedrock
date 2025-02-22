# Blog Generation using AWS Lambda and AWS Bedrock

A Python-based application that leverages AWS services and generative AI to automatically generate blog posts. It integrates a Streamlit-powered GUI with AWS Lambda and AWS Bedrock to deliver an interactive, serverless solution.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Getting Started](#getting-started)
- [CI/CD](#cicd)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains the code for blog generation using generative artificial intelligence. The application is written in Python and utilizes several AWS services, including AWS Lambda, AWS Bedrock, API Gateway, Cloudwatch, and S3. The Streamlit GUI makes it easy for users to interact with the system and generate blog posts effortlessly.

## Architecture

- **User Interface:**  
  Built with [Streamlit](https://streamlit.io) to provide an intuitive and interactive web-based experience.

- **API Layer:**  
  The Streamlit GUI makes API calls to an AWS Lambda function via API Gateway.

- **AI Inference:**  
  The Lambda function uses AWS Bedrock to access the `llama3-8b-instruct-v1:0` model (an open source model provided by Meta AI) for generating blog content.

- **Storage & Logging:**  
  Generated blog posts are stored in an S3 bucket, while logging is managed through AWS Cloudwatch.

- **Security:**  
  IAM roles are used to configure and securely manage access to AWS services.

## Features

- **Interactive Blog Generation:**  
  Quickly generate high-quality blog posts using advanced AI technology.

- **Serverless Infrastructure:**  
  Leverage AWS Lambda for cost-effective, scalable execution.

- **Automated CI/CD:**  
  Updates pushed to the `main` branch trigger an automatic deployment of the Lambda function via GitHub Actions.

- **Comprehensive AWS Integration:**  
  Utilizes API Gateway, Cloudwatch, and S3 to deliver a robust and maintainable solution.

## Getting Started

### Prerequisites

- Python 3.x
- An AWS account with the necessary permissions
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/4ashutosh98/Blog-Generation-using-AWS-Lambda-and-AWS-Bedrock.git
   cd Blog-Generation-using-AWS-Lambda-and-AWS-Bedrock
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials:**  
   Ensure your AWS credentials and environment variables are properly set up to allow access to AWS services.

### Running Locally

To run the Streamlit application locally:

```bash
streamlit run app.py
```

## CI/CD

This project features CI/CD capabilities using GitHub Actions. Any updates pushed to the `main` branch automatically deploy the updated `lambda_function.py` to AWS Lambda, ensuring seamless integration and deployment.

## Deployment

The application is deployed on [share.streamlit.io](https://share.streamlit.io) so that users can try out the blog generation functionality without any local setup.

**Access the live demo here:**  
[Blog Generation App](https://blog-generation-using-aws-lambda-and-aws-bedrock-ash.streamlit.app/)

## Contributing

Contributions are welcome! If you'd like to improve the project or fix an issue, please feel free to fork the repository and create a pull request. For major changes, open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


