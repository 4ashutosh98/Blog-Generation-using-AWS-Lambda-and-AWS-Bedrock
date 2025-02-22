import boto3
import botocore.config
import json
from datetime import datetime

def blog_generate_using_bedrock(blogtopic:str) -> str:
    prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]
    """

    body = {
        "prompt": prompt,
        "max_gen_len":512,
        "temperature":0.5,
        "top_p":0.9
    }

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name = "us-east-1",
            config=botocore.config.Config(
                read_timeout=300,
                retries={"max_attempts":3}
            )
        )
        response = bedrock.invoke_model(body = json.dumps(body), modelId = "meta.llama3-8b-instruct-v1:0")
        response_content = json.loads(response.get('body').read())
        print(response_content)
        blog_details = response_content['generation']
        return blog_details
    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""
    
def save_blog_details_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Key = s3_key, Bucket = s3_bucket, Body = generate_blog)
        print("Generated blog saved to S3")
    
    except Exception as e:
        print(f"Error saving blog to S3: {e}")
    
def lambda_handler(event, context):
    # TODO implement

    event = json.loads(event['body'])
    blogtopic = event['blog_topic']
    generate_blog = blog_generate_using_bedrock(blogtopic=blogtopic)


    if generate_blog:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        s3_key = f"blog-out/{current_time}.txt"
        s3_bucket = "awsbedrockbloggenerationash"
        save_blog_details_s3(s3_key=s3_key, s3_bucket=s3_bucket,generate_blog=generate_blog)

    else:
        print("Error generating blog")

    return {
        'statusCode': 200,
        'body': json.dumps('Blog generation complete!')
    }
