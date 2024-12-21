from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

# Fonction pour connecter à la base de données
#def connect_db():
    #db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
   # print(f"Chemin de la base de données : {db_path}")  # Pour vérifier le chemin
   # return sqlite3.connect(db_path)

def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    if not os.path.exists(db_path):
        print(f"Erreur : La base de données est introuvable au chemin : {db_path}")
    else:
        print(f"Connexion à la base de données : {db_path}")
    return sqlite3.connect(db_path)

# Fonction pour récupérer les exécutables depuis la base de données
def fetch_executables_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, file_path FROM executables")
    executables = cursor.fetchall()
    print(f"Contenu de la table executables : {executables}")  # Pour voir les données
    conn.close()
    return executables

# Route de test
@app.route('/')
def home():
    return 'Hello, world!'

# Route pour obtenir les exécutables
@app.route('/executables', methods=['GET'])
def get_executables():
    executables = fetch_executables_from_db()
    results = [{"id": exe[0], "file_path": exe[1]} for exe in executables]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
