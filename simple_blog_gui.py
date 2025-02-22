import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Set the URL for the AWS Lambda function
LAMBDA_URL = os.getenv("LAMBDA_URL")


# Streamlit GUI
st.title("Blog Generator")

# Input for blog topic
blog_topic = st.text_input("Enter the blog topic:")

# Button to generate blog
if st.button("Generate Blog"):
    if blog_topic:
        # Prepare the payload
        payload = {
            "blog_topic": blog_topic
        }
        
        # Send POST request to the Lambda function
        response = requests.post(LAMBDA_URL, json=payload, timeout=200)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Display the generated blog
            response_data = response.json()
            blog_content = response_data['blog']
            st.subheader("Generated Blog:")
            st.write(blog_content)
        else:
            st.error("Error generating blog. Please try again.")
    else:
        st.warning("Please enter a blog topic.")
