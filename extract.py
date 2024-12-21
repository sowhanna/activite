from flask import Flask, jsonify
import os
import sqlite3
from extract import extract_features  # Importation de la fonction d'extraction

app = Flask(__name__)

# Connexion à la base de données SQLite
def connect_db():
    # Connexion à la base de données SQLite, située dans le même dossier
    conn = sqlite3.connect('database.db')  # Nom de la base de données
    return conn

# Récupère les fichiers exécutables de la base de données
def fetch_executables_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_path FROM executables")  # La table 'executables'
    executables = cursor.fetchall()
    conn.close()
    return executables

# Route principale de l'API qui renvoie un message de bienvenue
@app.route('/')
def home():
    return 'Bonjour le monde!'

# Route pour récupérer les caractéristiques des exécutables
@app.route('/executables', methods=['GET'])
def get_executables():
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
