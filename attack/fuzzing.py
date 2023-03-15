import socket
import random
import string
import time

def generate_random_data(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def udp_fuzzer(target_ip, target_port, delay=0.1, max_length=1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        random_data = generate_random_data(random.randint(1, max_length))
        sock.sendto(random_data.encode(), (target_ip, target_port))
        print(f"Envoyé {len(random_data)} octets à {target_ip}:{target_port}")
        time.sleep(delay)

def main():
    target_ip = input("Entrez l'adresse IP de la cible: ")
    target_port = int(input("Entrez le port de la cible: "))
    delay = float(input("Entrez le délai entre les envois (en secondes): "))
    max_length = int(input("Entrez la longueur maximale des données aléatoires: "))

    udp_fuzzer(target_ip, target_port, delay, max_length)

if __name__ == "__main__":
    main()
