import sqlite3
import os
import shutil
os.system("pkill chrome")

chrome_cache_path = os.path.expanduser('~/.cache/google-chrome')

shutil.rmtree(chrome_cache_path)

print("Cache de Google Chrome supprimé avec succès!")

chrome_history_path = os.path.expanduser('~/.config/google-chrome/Default/History')

# Se connecter à la base de données de l'historique de Chrome
conn = sqlite3.connect(chrome_history_path)
c = conn.cursor()

# Supprimer toutes les entrées de l'historique de navigation
c.execute("DELETE FROM urls")

# Enregistrer les modifications et fermer la connexion
conn.commit()
conn.close()

print("Historique de navigation de Google Chrome supprimé avec succès!")
