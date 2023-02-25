import socket

def detect_open_ports():
    # Liste des ports autorisés
    whitelist = [22, 80, 443]

    # Adresse IP de la machine locale
    ip_address = '127.0.0.1'

    # Vérification des ports de 1 à 1024 sur la machine locale
    for port in range(1, 65535):
        try:
            # Création d'une connexion socket vers l'adresse IP et le port actuels
            with socket.create_connection((ip_address, port), timeout=0.5) as sock:
                # Si la connexion réussit et que le port n'est pas sur la liste blanche
                if port not in whitelist:
                   try:
                        protocol_name = socket.getservbyport(port)
                        print(f"Le port {port} est associé au protocole {protocol_name}.")
                   except OSError:
                        print(f"Le port {port} n'est pas associé à un protocole connu.")

        # Si la connexion échoue, le port est fermé
        except (socket.timeout, ConnectionRefusedError):
            pass

# Appel de la fonction detect_open_ports()
detect_open_ports()
