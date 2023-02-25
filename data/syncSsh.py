import paramiko
import os

# spécifiez les détails de connexion SSH
ssh_host = 'adresse_IP_du_serveur'
ssh_port = 22
ssh_user = 'utilisateur_ssh'
ssh_pass = 'mot_de_passe_ssh'

# spécifiez le chemin d'accès au fichier que vous souhaitez transférer
local_file_path = '/chemin/vers/le/fichier_local.txt'

# spécifiez le chemin d'accès et le nom de fichier pour le serveur distant
remote_path = '/chemin/vers/le/fichier_sur_le_serveur.txt'

# établir une connexion SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ssh_host, port=ssh_port, username=ssh_user, password=ssh_pass)

# vérifier la redondance avant de transférer le fichier
sftp = ssh.open_sftp()
try:
    sftp.stat(remote_path)
    print("Le fichier existe déjà sur le serveur, pas de transfert nécessaire.")
except FileNotFoundError:
    sftp.put(local_file_path, remote_path)
    print("Le fichier a été transféré avec succès sur le serveur.")
sftp.close()

# fermer la connexion SSH
ssh.close()
