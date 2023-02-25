import ipaddress

# Demander à l'utilisateur de saisir l'adresse IP et le masque de sous-réseau
ip_address = input("Entrez l'adresse IP : ")
subnet_mask = input("Entrez le masque de sous-réseau : ")

# Créer un objet d'adresse IP à partir de l'adresse IP et du masque de sous-réseau
network = ipaddress.IPv4Network(ip_address + '/' + subnet_mask, strict=False)

# Trouver l'adresse de début et l'adresse de fin de la plage
start_ip = network.network_address
end_ip = network.broadcast_address

# Afficher les adresses de début et de fin
print("Adresse de début de la plage d'adresses IP : ", start_ip)
print("Adresse de fin de la plage d'adresses IP : ", end_ip)
