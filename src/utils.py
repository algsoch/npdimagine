import json
import os
from datetime import datetime

def load_json(file_path):
    """Loads JSON data from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON from {file_path}: {e}")
        return {}

def save_json(file_path, data):
    """Saves data to a JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving JSON to {file_path}: {e}")

def log_message(log_file, message):
    """Writes a log message with timestamp."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now().isoformat()} - {message}\n")
