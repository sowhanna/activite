from flask import Flask, request, jsonify
from extract import extract_features

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    features = extract_features(file)
    return jsonify(features)

if __name__ == "__main__":
    app.run(debug=True)
