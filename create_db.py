import sqlite3
import os

def create_db():
    # Définir le chemin de la base de données
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

    # Connexion à la base de données SQLite (cela la crée si elle n'existe pas)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Créer une table 'executables' si elle n'existe pas déjà
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS executables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL
    )
    ''')

    # Ajouter quelques fichiers exécutables pour l'exemple
    executable_path = r'C:\Users\ANNA\Desktop\iso et logiciel\VC_redist.x64.exe'

    # Assurez-vous que le chemin est correct avant d'ajouter dans la base de données
    cursor.execute('''
    INSERT INTO executables (file_path) VALUES (?)
    ''', (executable_path,))

    # Commit les changements et ferme la connexion
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Base de données créée et exécutables ajoutés.")
