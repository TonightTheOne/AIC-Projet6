#! /usr/bin/env python3
# -*- coding:utf8 -*-

# Import des modules nécessaires
import paramiko
import sys
from getpass import getpass

# Variable pour la connexion SSH
hostname = input("Entrez l'adresse IP pour la connexion SSH: ")
username = input("Entrez l'utilisateur: ")
password = getpass("Entrez le mot de passe: ")

# Initialise la connexion SSH
client = paramiko.SSHClient()

# Ajoutes les hosts connus
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# Variable de la commande qui va être envoyé par paramiko pour le backup avec rsync
backup = "rsync -av --del --stats --force --filter '- .thumbnails/' --filter '- .Trash/' \
--filter '- *.tmp' --filter '- *.iso' --filter '- lost+found/' --filter '- .cache/' \
--filter '- .beagle/' /home/ /media/Partage_Backup/"+ str(hostname)

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

