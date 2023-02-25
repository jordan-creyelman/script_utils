import subprocess
import os
import re
from datetime import datetime

# Vérifier si des connexions non autorisées ont été enregistrées dans les logs
def check_unauthorized_connections(log_file):
    unauthorized_ips = []
    with open(log_file, 'r') as f:
        for line in f:
            # Vérifier si le message de log contient une adresse IP non autorisée
            if re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line) and not is_ip_authorized(line):
                ip = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line).group()
                unauthorized_ips.append(ip)
    if unauthorized_ips:
        print(f"Des connexions non autorisées ont été enregistrées dans le fichier journal {log_file}: {', '.join(unauthorized_ips)}")
    else:
        print(f"Aucune connexion non autorisée n'a été enregistrée dans le fichier journal {log_file}")

# Vérifier si une adresse IP est autorisée
def is_ip_authorized(line):
    # Vérifier si l'adresse IP est dans la liste des adresses IP autorisées
    authorized_ips = ['127.0.0.1', '192.168.0.1']
    ip = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line).group()
    if ip in authorized_ips:
        return True
    else:
        return False

# Vérifier si l'heure des logs a été modifiée
def check_log_time(log_file):
    log_mod_time = os.path.getmtime(log_file)
    current_time = datetime.now().timestamp()
    if current_time - log_mod_time > 3600:
        print(f"L'heure du fichier journal {log_file} a été modifiée !")
    else:
        print(f"L'heure du fichier journal {log_file} n'a pas été modifiée.")

        
        
def analyze_system_logs():
     cmd = 'grep -iE "fail|error|refused|denied" /var/log/*'
     try:
         output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
         if output:
             print('WARNING: Suspicious events found in system logs!')
     except:
         pass
analyze_system_logs();

# Chemin du fichier journal à vérifier
log_file = '/var/log/syslog'

# Vérifier les connexions non autorisées dans le fichier journal
check_unauthorized_connections(log_file)

# Vérifier si l'heure du fichier journal a été modifiée
check_log_time(log_file)
