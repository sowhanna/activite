import os

def extract_features(executable_path):
    # Liste des 7 caractéristiques à extraire
    features = {
        "file_size": os.path.getsize(executable_path),  # Taille du fichier en octets
        "file_name": os.path.basename(executable_path),  # Nom du fichier
        "executable_path": executable_path,  # Chemin complet du fichier
        "is_executable": os.access(executable_path, os.X_OK),  # Vérifie si le fichier est exécutable
        "creation_time": os.path.getctime(executable_path),  # Date de création du fichier
        "last_modified_time": os.path.getmtime(executable_path),  # Date de dernière modification
        "last_access_time": os.path.getatime(executable_path)  # Date du dernier accès
    }
    return features
