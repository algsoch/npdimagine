import time

def execute_task(task):
    time.sleep(2)  # Simulate processing
    return f"Task '{task}' executed successfully."

## utils.py - Utility Functions
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

## llm_agent.py - LLM Integration
import openai
import os

def query_llm(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']