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
@app.route('/executables/features', methods=['GET'])
def get_executables_features():
    executables = fetch_executables_from_db()
    all_features = []
    
    for exe in executables:
        executable_path = exe[1]  # Le chemin de l'exécutable depuis la base de données
        if os.path.exists(executable_path):
            features = extract_features(executable_path)  # Extraction des caractéristiques
            all_features.append({
                "id": exe[0],  # ID de l'exécutable
                "file_path": executable_path,
                "features": features
            })
        else:
            all_features.append({
                "id": exe[0],
                "file_path": executable_path,
                "features": {"error": "Executable non trouvé"}
            })
    
    return jsonify(all_features), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
