import os

cookie_path = os.path.expanduser("~/.config/google-chrome/Default/Cookies")
os.remove(cookie_path)
print("Les cookies de Google Chrome ont été supprimés avec succès.")
