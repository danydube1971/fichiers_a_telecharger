"""Ce script Python effectue les tâches suivantes:

1. Il crée une interface utilisateur graphique (GUI) qui permet à l'utilisateur de sélectionner un dossier de destination pour les fichiers à télécharger.
2. Il ouvre un fichier texte nommé `download.txt`, qui doit être dans le même répertoire que le script. Ce fichier doit contenir une liste d'URLs, une par ligne, 
qui représentent les fichiers à télécharger.
3. Pour chaque URL de la liste, le script lance un processus de téléchargement parallèle (en utilisant plusieurs threads). 
Cela signifie que plusieurs fichiers peuvent être téléchargés en même temps, ce qui peut accélérer le processus si vous avez beaucoup de fichiers à télécharger.
4. Pendant le téléchargement d'un fichier, le script affiche une barre de progression dans la console pour montrer combien de données ont déjà été téléchargées.
5. Le script met un délai d'attente de 10 secondes pour chaque URL. Si le téléchargement n'a pas commencé après 10 secondes, il arrête d'essayer de télécharger ce fichier, 
affiche un message d'erreur, et passe à l'URL suivante.
6. Les fichiers téléchargés sont enregistrés dans le dossier que l'utilisateur a sélectionné au début.
7. Si une erreur se produit lors du téléchargement d'un fichier (par exemple, si l'URL est invalide ou si la connexion Internet est interrompue), 
le script affiche un message d'erreur mais continue d'essayer de télécharger les autres fichiers."""

# Assurez-vous d'avoir un fichier download.txt dans le même répertoire que votre script, qui contient une URL de fichier par ligne. Ces URL sont les fichiers qui seront téléchargés.
# Veuillez installer les modules suivantes via la commande: pip3 install requests tqdm tkinter
import os
import tkinter as tk
from tkinter import filedialog
from concurrent.futures import ThreadPoolExecutor
import requests
from tqdm import tqdm

# Cette fonction télécharge un fichier depuis une URL vers un dossier de destination
def download_file(url, destination_folder):
    # Nous récupérons le nom du fichier depuis l'URL
    local_filename = url.split('/')[-1]
    # Nous combinons le dossier de destination avec le nom du fichier
    local_filename = os.path.join(destination_folder, local_filename)

    try:
        # Nous effectuons une requête GET sur l'URL avec un délai d'attente de 10 secondes
        with requests.get(url, stream=True, timeout=10) as r:
            # Nous vérifions que la requête a réussi
            r.raise_for_status()

            # Nous récupérons la taille totale du fichier
            total_size = int(r.headers.get('content-length', 0))

            # Nous ouvrons le fichier en mode écriture binaire
            with open(local_filename, 'wb') as f, tqdm(
                desc=local_filename,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                # Pour chaque bloc de données reçu
                for chunk in r.iter_content(chunk_size=1024):
                    # Nous écrivons les données dans le fichier
                    size = f.write(chunk)
                    # Nous mettons à jour la barre de progression
                    bar.update(size)
    # Si une exception est levée pendant le processus de téléchargement
    except (requests.exceptions.RequestException, Exception) as e:
        # Nous affichons un message d'erreur
        print(f"Erreur lors du téléchargement du fichier {url} : {str(e)}")

# Cette fonction ouvre une fenêtre de dialogue pour choisir le dossier de destination et lance le téléchargement des fichiers
def select_directory_and_download():
    # Nous créons une fenêtre Tkinter
    root = tk.Tk()
    # Nous la rendons invisible
    root.withdraw()

    # Nous ouvrons une fenêtre de dialogue pour choisir le dossier de destination
    folder_selected = filedialog.askdirectory()

    # Nous ouvrons le fichier download.txt et nous récupérons la liste des URLs
    with open('download.txt', 'r') as f:
        urls = f.read().splitlines()

    # Nous créons un pool de threads
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Pour chaque URL dans la liste
        for url in urls:
            # Nous lançons le téléchargement du fichier
            executor.submit(download_file, url, folder_selected)

# Nous lançons le programme
if __name__ == "__main__":
    select_directory_and_download()

