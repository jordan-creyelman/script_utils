import tarfile
import os
import datetime
import sys

# Vérifie que le dossier à sauvegarder a été fourni en entrée
if len(sys.argv) < 2:
    print("Usage: backup.py <folder_to_backup>")
    sys.exit(1)

# Dossier à sauvegarder
folder_to_backup = sys.argv[1]
name=sys.argv[2]

# Vérifie que le dossier à sauvegarder existe
if not os.path.isdir(folder_to_backup):
    print("Le dossier à sauvegarder n'existe pas.")
    sys.exit(1)

# Nom de l'archive
archive_name = name+"_"+"backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".tar.gz"

# Créer l'archive
with tarfile.open(archive_name, "w:gz") as tar:
    tar.add(folder_to_backup, arcname=os.path.basename(folder_to_backup))

print("Archive créée : ", archive_name)
