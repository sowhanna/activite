import os
import hashlib
import magic

def extract_features(file_path):
    """
    Cette fonction extrait 7 caractéristiques d'un fichier exécutable.
    """
    # 1. Nom du fichier
    file_name = os.path.basename(file_path)

    # 2. Taille du fichier
    file_size = os.path.getsize(file_path)

    # 3. Date de création
    creation_time = os.path.getctime(file_path)

    # 4. Date de dernière modification
    modification_time = os.path.getmtime(file_path)

    # 5. Accessibilité en tant qu'exécutable
    is_executable = os.access(file_path, os.X_OK)

    # 6. Type MIME (assurez-vous d'installer python-magic)
    mime_type = magic.from_file(file_path, mime=True)

    # 7. Hash MD5
    md5_hash = get_md5(file_path)

    # Retourner les caractéristiques sous forme de dictionnaire
    features = {
        "file_name": file_name,
        "file_size": file_size,
        "creation_time": creation_time,
        "modification_time": modification_time,
        "is_executable": is_executable,
        "mime_type": mime_type,
        "md5_hash": md5_hash
    }
    return features

# Fonction pour obtenir le hash MD5 d'un fichier
def get_md5(file_path):
    """
    Cette fonction génère le hash MD5 d'un fichier.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
