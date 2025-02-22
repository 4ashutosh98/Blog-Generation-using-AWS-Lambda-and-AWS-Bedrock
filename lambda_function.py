import boto3
import botocore.config
import json
from datetime import datetime
import re

def clean_response(response_text):
    """Removes unwanted text after the blog content"""
    cleaned_text = re.split(r"\[/INST\]", response_text, maxsplit=1)[0]
    return cleaned_text.strip()

def blog_generate_using_bedrock(blogtopic:str) -> str:
    prompt = f"""You are a professional blog writer. Write a well-structured, 200-word blog on the topic {blogtopic}. 
    DO NOT include any additional explanation, disclaimers, or instructions. Only return the blog content.
    Limit your response to 300 words.
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
        raw_blog_text = response_content.get('generation', '')
        blog_details = clean_response(raw_blog_text)
        return blog_details
    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""
    
def save_blog_details_s3(s3_key, s3_bucket, generated_blog):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Key = s3_key, Bucket = s3_bucket, Body = generated_blog)
        print("Generated blog saved to S3")
    
    except Exception as e:
        print(f"Error saving blog to S3: {e}")
    
def lambda_handler(event, context):
    # TODO implement
    event = json.loads(event['body'])
    blogtopic = event['blog_topic']
    generated_blog = blog_generate_using_bedrock(blogtopic=blogtopic)


    if generated_blog:
        # Save to S3
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        s3_key = f"blog-out/{current_time}.txt"
        s3_bucket = "awsbedrockbloggenerationash"
        save_blog_details_s3(s3_key=s3_key, s3_bucket=s3_bucket, generated_blog=generated_blog)

        # Return success response with generated blog
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Blog generation complete!',
                'blog': generated_blog  # Including the generated blog in response
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    else:
        # Return failure response
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error generating blog'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
