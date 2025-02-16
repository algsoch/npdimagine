import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve API token from .env
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

# AI Proxy API URL
AIPROXY_URL = "https://api.ai-proxy.com/generate"

def call_llm(prompt):
    """
    Calls the GPT-4o-Mini LLM via AI Proxy to process a given prompt.

    :param prompt: The prompt string to send to the LLM.
    :return: The response from the LLM as a string.
    """
    if not AIPROXY_TOKEN:
        raise ValueError("AIPROXY_TOKEN is missing! Set it in the .env file.")

    headers = {
        "Authorization": f"Bearer {AIPROXY_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "prompt": prompt,
        "max_tokens": 200
    }

    try:
        response = requests.post(AIPROXY_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json().get("text", "").strip()
    except requests.exceptions.RequestException as e:
        return f"LLM API error: {str(e)}"

# Example Function: Extract Sender Email from Email Content
def extract_email_sender(email_content):
    prompt = f"Extract the sender's email address from this email:\n\n{email_content}"
    return call_llm(prompt)

# Example Function: Extract Credit Card Number from Image
def extract_credit_card_number(image_path):
    prompt = f"Extract the credit card number from the image at {image_path}."
    return call_llm(prompt)

# Example Function: Find Similar Comments
def find_most_similar_comments(comments):
    prompt = f"Find the two most similar comments from this list:\n{comments}"
    result = call_llm(prompt)
    return result.split("\n")[:2] if result else ("", "")
