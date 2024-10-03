# client_app.py
from logging import INFO, getLogger
import flask
from flask import jsonify
import requests
import os

import monitoring

app = flask.Flask(__name__)

logger = getLogger(__name__)
logger.setLevel(INFO)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

@app.route("/call_info_log")
def call_info_log():
    try:
        print(f"{BACKEND_URL}/info_log")
        response = requests.get(f"{BACKEND_URL}/info_log")
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling info_log: {e}")
        return jsonify({"error": f"Failed to retrieve info log: {e}"}), 500

@app.route("/call_error_log")
def call_error_log():
    try:
        response = requests.get(f"{BACKEND_URL}/error_log")
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling error_log: {e}")
        return jsonify({"error": "Failed to retrieve error log"}), 500

@app.route("/call_get_data")
def call_get_data():
    try:
        response = requests.get(f"{BACKEND_URL}/api/data")
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling get_data: {e}")
        return jsonify({"error": "Failed to retrieve data"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)