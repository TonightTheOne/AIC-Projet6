#! /usr/bin/env python3
# -*- coding:utf8 -*-

# Import des modules nécessaires 
import paramiko
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

# Variable de la commande qui va être envoyé par paramiko
cmd = "sudo cat /etc/passwd | awk -F: '{print $ 1}'"

# Exécution de la commande
stdin, stdout, stderr = client.exec_command(cmd)

# Lire la sortie standard et l'afficher
print(stdout.read().decode())

# Affiche les erreurs si il y en a
err = stderr.read().decode()
if err:
    print(err)
    
# Ferme la connexion
client.close()

