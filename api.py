from flask import Flask, jsonify
import sqlite3
import os
from extract import extract_features  # Importer la fonction d'extraction

app = Flask(__name__)

# Fonction pour connecter à la base de données SQLite
def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    return sqlite3.connect(db_path)

# Fonction pour récupérer tous les exécutables depuis la base de données
def fetch_executables_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_path FROM executables")
    executables = cursor.fetchall()
    conn.close()
    return executables

# Route principale pour tester l'API
@app.route('/')
def home():
    return "API en fonctionnement !"

# Route pour obtenir les 7 caractéristiques de chaque exécutable
@app.route('/executables', methods=['GET'])
def get_executables():
    executables = fetch_executables_from_db()
    results = [{"id": exe[0], "file_path": exe[1]} for exe in executables]
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
