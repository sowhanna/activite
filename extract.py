# extractor.py
import os
import hashlib
import magic

def extract_features(file_path):
    """
    Cette fonction extrait 7 caractéristiques d'un fichier exécutable.
    """
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    is_executable = os.access(file_path, os.X_OK)
    mime_type = magic.from_file(file_path, mime=True)
    md5_hash = get_md5(file_path)

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

def get_md5(file_path):
    """
    Cette fonction génère le hash MD5 d'un fichier.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
