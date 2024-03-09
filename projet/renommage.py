import os

dossier_images = "./"
modele_nom = "ethan{}.png"

# Vérification de l'existence du dossier
if not os.path.isdir(dossier_images):
    print("Le dossier spécifié n'existe pas.")
    exit()

# Liste tous les fichiers dans le dossier
fichiers = os.listdir(dossier_images)

# Filtre uniquement les fichiers avec l'extension .png
images = [fichier for fichier in fichiers if (fichier.lower().endswith('.jpeg') or fichier.lower().endswith('.jpg') or fichier.lower().endswith('.png'))]

# Parcours des images et renommage
for i, image in enumerate(images, 1):
    ancien_nom = os.path.join(dossier_images, image)
    nouveau_nom = os.path.join(dossier_images, modele_nom.format(i))
    os.rename(ancien_nom, nouveau_nom)
    print(f"Image {ancien_nom} renommée en {nouveau_nom}.")
