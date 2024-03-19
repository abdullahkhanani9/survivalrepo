# api.py

from flask import Flask, request, jsonify
from model import predict_survival

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    passenger_data = request.json
    prediction = predict_survival(passenger_data)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
