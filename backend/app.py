from logging import INFO, getLogger

import flask
from flask import jsonify

# Import the monitoring configuration
import monitoring

logger = getLogger(__name__)
logger.setLevel(INFO)

app = flask.Flask(__name__)

@app.route("/info_log")
def info_log():
    message = "Correlated info log"
    logger.info(message)
    return message


@app.route("/error_log")
def error_log():
    message = "Correlated error log"
    logger.error(message)
    return message

@app.route('/api/data')
def get_data():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)