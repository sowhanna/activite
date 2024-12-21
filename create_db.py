import sqlite3
import os

def create_db():
    # Définir le chemin de la base de données
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

    # Connexion à la base de données SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Créer une table 'executables' si elle n'existe pas déjà
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS executables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL UNIQUE
    )
    ''')

    # Exemple d'exécutable à ajouter
    executable_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'executables', 'VC_redist.x64.exe')

    # Vérification de l'existence de l'exécutable avant insertion
    cursor.execute("SELECT * FROM executables WHERE file_path = ?", (executable_path,))
    exists = cursor.fetchone()

    if not exists:
        # Insérer un nouvel exécutable
        cursor.execute('''
        INSERT INTO executables (file_path) VALUES (?)
        ''', (executable_path,))
        print("Chemin ajouté à la base de données.")
    else:
        print("Chemin déjà existant dans la base de données.")

    # Commit des changements et fermer la connexion
    conn.commit()
    conn.close()
    print("Base de données mise à jour.")

if __name__ == "__main__":
    create_db()
