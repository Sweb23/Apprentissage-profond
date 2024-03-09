from PIL import Image
import os

# Chemin du dossier contenant les images
dossier_images = "./"
# Chemin du sous-dossier où enregistrer les images redimensionnées
sous_dossier = "images_redimensionnees"

# Vérification de l'existence du dossier
if not os.path.isdir(dossier_images):
    print("Le dossier spécifié n'existe pas.")
    exit()

# Création du sous-dossier s'il n'existe pas
sous_dossier_path = os.path.join(dossier_images, sous_dossier)
os.makedirs(sous_dossier_path, exist_ok=True)

# Liste tous les fichiers dans le dossier
fichiers = os.listdir(dossier_images)

# Filtre uniquement les fichiers avec l'extension .png
images = [fichier for fichier in fichiers if (fichier.lower().endswith('.jpeg') or fichier.lower().endswith('.jpg') or fichier.lower().endswith('.png'))]

# Redimensionnement et enregistrement des images
for image in images:
    chemin_image_entree = os.path.join(dossier_images, image)
    chemin_image_sortie = os.path.join(sous_dossier_path, image)
    
    # Ouvre l'image avec PIL
    img = Image.open(chemin_image_entree)
    # Redimensionne l'image en 128x128
    img = img.resize((128, 128))
    # Enregistre l'image redimensionnée dans le sous-dossier
    img.save(chemin_image_sortie)

    print(f"Image {chemin_image_entree} redimensionnée et enregistrée dans {chemin_image_sortie}.")
