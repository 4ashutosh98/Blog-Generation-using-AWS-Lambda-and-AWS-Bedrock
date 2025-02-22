# Blog-Generation-using-AWS-Lambda-and-AWS-Bedrock

This repo contains the code files necessary for blog generation using Generative Artificial Intelligence.
The code is written in Python and utilizes various services provided by Amazon Web Services (AWS).

The `Streamlit` GUI makes an API call to the `AWS lambda` function, which then uses the `AWS Bedrock` service to generate a blog post.
The generated blog post is then returned to the API caller.

The LLM used for inferencing is `llama3-8b-instruct-v1:0` which is an open source model provided by Meta AI.
This model is accessed from the `AWS Bedrock` service.

Other services from `AWS` used in this app include `API Gateway` for API calls, `Cloudwatch` for logging purposes and `S3` bucket for storing the generated blog posts.
IAM roles are also used for configuration of the AWS services.

This project also has CI/CD capabilities. When any updates are pushed to `main` branch of this repository, the updated `lambda_function.py` is automatically deployed to `AWS Lambda` using `GitHub Actions`.