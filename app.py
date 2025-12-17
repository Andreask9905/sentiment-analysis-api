import os
from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "Sentiment Analysis API is running 🚀",
        "usage": {
            "endpoint": "/predict",
            "method": "POST",
            "body": {
                "text": "Your text here"
            }
        }
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    sentiment = predict_sentiment(text)
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
