from flask import Flask, jsonify
import os
import sqlite3
from extract import extract_features  # Importation de la fonction d'extraction
import magic

app = Flask(__name__)

# Connexion à la base de données SQLite
def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')  # Chemin vers la base de données
    conn = sqlite3.connect(db_path)
    return conn

# Récupère les fichiers exécutables de la base de données
def fetch_executables_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_path FROM executables")  # Adaptez la requête selon votre BD
    executables = cursor.fetchall()  # Récupère tous les exécutables
    conn.close()
    return executables

# Route principale de l'API qui renvoie les caractéristiques de tous les exécutables
@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/executables', methods=['GET'])
def get_executables():
    """
    Parcourt la base de données et retourne les caractéristiques des exécutables.
    """
    executables = fetch_executables_from_db()
    results = []
    for executable in executables:
        file_path = executable[1]  # Le chemin du fichier est à l'index 1
        if os.path.isfile(file_path):  # Vérifie si c'est un fichier existant
            features = extract_features(file_path)  # Appel à la fonction d'extraction
            results.append(features)
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
