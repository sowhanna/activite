from flask import Flask, jsonify
import os
import sqlite3
from extract import extract_features  # Importation depuis extractor.py

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

def fetch_executables_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_path FROM executables")
    executables = cursor.fetchall()
    conn.close()
    return executables
@app.route('/')
def home():
    return 'Hello, world!'  # Assurez-vous que cette route est bien définie


@app.route('/executables', methods=['GET'])
def get_executables():
    executables = fetch_executables_from_db()
    results = []
    for executable in executables:
        file_path = executable[1]
        if os.path.isfile(file_path):
            features = extract_features(file_path)
            results.append(features)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
