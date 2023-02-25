import requests

def get_public_ip():
    # Interroger un service en ligne pour récupérer l'adresse IP publique
    response = requests.get('https://api.ipify.org')
    # Extraire l'adresse IP de la réponse
    public_ip = response.text.strip()
    return public_ip

# Appeler la fonction pour récupérer l'adresse IP publique
ip = get_public_ip()
print("Votre adresse IP publique est :", ip)
