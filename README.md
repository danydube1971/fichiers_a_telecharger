# fichiers_a_telecharger
Permet de télécharger une liste de fichiers inscrit (url) dans un fichier nommé download.txt

Ce script Python effectue les tâches suivantes:

1. Il crée une interface utilisateur graphique (GUI) qui permet à l'utilisateur de sélectionner un dossier de destination pour les fichiers à télécharger.
2. Il ouvre un fichier texte nommé `download.txt`, qui doit être dans le même répertoire que le script. Ce fichier doit contenir une liste d'URLs, une par ligne, qui représentent les fichiers à télécharger.
3. Pour chaque URL de la liste, le script lance un processus de téléchargement parallèle (en utilisant plusieurs threads). Cela signifie que plusieurs fichiers peuvent être téléchargés en même temps, ce qui peut accélérer le processus si vous avez beaucoup de fichiers à télécharger.
4. Pendant le téléchargement d'un fichier, le script affiche une barre de progression dans la console pour montrer combien de données ont déjà été téléchargées.
5. Le script met un délai d'attente de 10 secondes pour chaque URL. Si le téléchargement n'a pas commencé après 10 secondes, il arrête d'essayer de télécharger ce fichier, affiche un message d'erreur, et passe à l'URL suivante.
6. Les fichiers téléchargés sont enregistrés dans le dossier que l'utilisateur a sélectionné au début.
7. Si une erreur se produit lors du téléchargement d'un fichier (par exemple, si l'URL est invalide ou si la connexion Internet est interrompue), le script affiche un message d'erreur mais continue d'essayer de télécharger les autres fichiers.

-------------------

Assurez-vous d'avoir un fichier *download.txt* dans le même répertoire que votre script, qui contient une URL de fichier par ligne. Ces URL sont les fichiers qui seront téléchargés.

Veuillez installer les modules suivantes via la commande: **pip3 install requests tqdm tkinter**

--------------------

***Comment utiliser le script***

Placer le script *fichiers à télécharger.py* dans le même dossier que le fichier *download.txt* (qui contient les url, un par ligne, à télécharger)

Ouvrir un terminal et taper la commande: **python3 "fichiers à télécharger.py"**

