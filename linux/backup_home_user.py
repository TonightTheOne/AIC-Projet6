#! /usr/bin/env python3
# -*- coding:utf8 -*-

# Import des modules nécessaires
import paramiko

# Variable pour la connexion SSH
hostname = input("Entrez l'adresse IP pour la connexion SSH: ")
username = input("Entrez l'utilisateur: ")
keyrsa = "/home/steve/.ssh/id_rsa.pub" # Modifier avec votre chemin

# Initialise la connexion SSH
client = paramiko.SSHClient()

# Ajoutes les hosts connus
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, key_filename=keyrsa)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# Variable de la commande qui va être envoyé par paramiko pour le backup avec rsync
backup = "sudo rsync -avz --no-o --no-g --del --stats --force --filter '- .thumbnails/' --filter '- .Trash/' \
--filter '- *.tmp' --filter '- *.iso' --filter '- lost+found/' --filter '- .cache/' \
--filter '- .beagle/' /home/ /mnt/backup-partage/"+ str(hostname)

# Exécution de la commande
stdin, stdout, stderr = client.exec_command(backup)

# Lire la sortie standard et l'afficher
print(stdout.read().decode())

# Affiche les erreurs si il y en a
err = stderr.read().decode()
if err:
    print(err)
    
# Ferme la connexion
client.close()

