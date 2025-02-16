## app.py - Main API
from flask import Flask, request, jsonify
import os
from src.tasks import execute_task
from src.utils import read_file

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_task():
    task = request.args.get("task")
    if not task:
        return jsonify({"error": "Task description is required"}), 400
    
    result = execute_task(task)
    return jsonify({"message": result}), 200

@app.route('/read', methods=['GET'])
def read():
    file_path = request.args.get("path")
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    content = read_file(file_path)
    return jsonify({"content": content}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)