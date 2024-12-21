import os

def extract_features(file_path):
    # Exemple : Vous pouvez utiliser des bibliothèques spécifiques pour analyser un exécutable
    features = {
        "file_name": os.path.basename(file_path),
        "file_size": os.path.getsize(file_path),
        # Ajouter d'autres analyses spécifiques
    }
    return features

def process_executables(folder_path):
    results = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            features = extract_features(file_path)
            results.append(features)
    return results

if __name__ == "__main__":
    folder = "chemin/vers/dossier/executables"
    features_list = process_executables(folder)
    print(features_list)
