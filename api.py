from flask import Flask, jsonify
import os
import sqlite3
from extract import extract_features  # Importation de la fonction d'extraction
import magic

app = Flask(__name__)
print("python-magic version:", magic.__version__)
# Connexion à la base de données SQLite
def connect_db():
    """
    Connexion à la base de données SQLite.
    Changez cette fonction si vous utilisez un autre SGBD (par exemple MySQL, PostgreSQL).
    """
    conn = sqlite3.connect('path_to_your_database.db')  # Remplacez par le chemin vers votre BD
    return conn

# Récupère les fichiers exécutables de la base de données
def fetch_executables_from_db():
    """
    Cette fonction récupère tous les exécutables de la base de données.
    Vous pouvez adapter la requête pour d'autres SGBD comme MySQL ou PostgreSQL.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_path FROM executables")  # Adaptez la requête selon votre BD
    executables = cursor.fetchall()  # Récupère tous les exécutables
    conn.close()
    return executables

# Route principale de l'API qui renvoie les caractéristiques de tous les exécutables
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
    # Vous pouvez aussi spécifier le port si nécessaire.
    app.run(host="0.0.0.0", port=5000)
