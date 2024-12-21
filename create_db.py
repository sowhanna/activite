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
        file_path TEXT NOT NULL UNIQUE
    )
    ''')

    # Ajouter un exemple d'exécutable (vous pouvez ajuster ce chemin en fonction de votre répertoire)
    executable_path = r'executables/VC_redist.x64.exe'  # Utilisez un chemin relatif ici

    # Vérifiez si le fichier existe déjà avant de l'insérer
    cursor.execute("SELECT * FROM executables WHERE file_path = ?", (executable_path,))
    exists = cursor.fetchone()

    if not exists:
        # Si le fichier n'existe pas, insérez-le
        cursor.execute('''
        INSERT INTO executables (file_path) VALUES (?)
        ''', (executable_path,))
        print("Chemin ajouté à la base de données.")
    else:
        print("Chemin déjà existant dans la base de données.")

    # Commit les changements et ferme la connexion
    conn.commit()
    conn.close()
    print("Base de données créée et mise à jour terminée.")
