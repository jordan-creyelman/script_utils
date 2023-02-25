import socket
import random
import os

def brouiller(ip):
    # Séparer l'adresse IP en octets
    ip_octets = ip.split('.')
    # Brouiller les trois derniers octets
    for i in range(1, 4):
        ip_octets[i] = str(random.randint(0, 255))
    # Rejoindre les octets brouillés en une seule adresse IP
    brouille_ip = '.'.join(ip_octets)
    return brouille_ip

# Adresse IP à brouiller
ip = '78.129.49.116'

# Brouiller l'adresse IP
brouille_ip = brouiller(ip)

# Vérifier le nom de l'interface réseau
interface = None
output = os.popen("ifconfig").read()
if "eth0" in output:
    interface = "eth0"
elif "enp0s3" in output:
    interface = "enp0s3"
elif "eth1" in output:
    interface = "eth1"
elif "wlp0s20f3" in output:
    interface="wlp0s20f3"
elif "enp0s31f6" in output:
    interface="enp0s31f6"
else:
    print("Interface réseau non trouvée")
    

# Modifier l'adresse IP de la machine
if interface:
    os.system(f"ifconfig {interface} {brouille_ip}")
    # Vérifier l'adresse IP modifiée
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Nouvelle adresse IP : ", ip_address)
