from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import numpy as np

app = Flask(__name__)
cors = CORS(app, origins="https://buhackathon.leenattia.repl.co")

# Load the pre-trained model
with open('trained_model.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)

@app.route('/', methods=["GET", "POST"])
def predict():
    try:
        data = request.json
        data_2d = np.array(data).reshape(1, -1)
        results = clf.predict(data_2d)
        return jsonify({'prediction': str(results[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8001)

