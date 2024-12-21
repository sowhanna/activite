from flask import Flask, request, jsonify
from extract import extract_features

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    features = extract_features(file)
    return jsonify(features)

#if __name__ == "__main__":
   # app.run(debug=True)
#if __name__ == "__main__":
   # app.run(host="0.0.0.0", port=5000)
    #import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Utilise le port fourni par Render ou 5000 par défaut
    app.run(host="0.0.0.0", port=port)
