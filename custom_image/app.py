import logging

from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

from src.inference import load_model, predict

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model
model = load_model()


# Use ProxyFix middleware for running behind a proxy
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route("/ping", methods=["GET"])
def ping():
    """
    Healthcheck function.
    """
    return "pong"


@app.route("/invocations", methods=["POST"])
def invocations():
    """
    Endpoint for model invocations.
    """
    try:
        image_data = request.data
        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        prediction = predict(image_data, model)
        return jsonify(prediction)
    except Exception as e:
        logger.exception(e)
        return jsonify({"error": "An error occurred during prediction"}), 500


if __name__ == "__main__":
    app.run(debug=True)
