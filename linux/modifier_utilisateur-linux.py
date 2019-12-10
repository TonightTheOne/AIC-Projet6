#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Import des modules nécessaires 
import paramiko
from getpass import getpass
import crypt

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

# Variable pour l'utilisateur à modifier
set_user = input("Entrez le nom de l'utilisateur à modifier: ")
set_new_user = input("Entrez le nouveau nom de l'utilisateur: ")
set_new_home = input("Entrez le nouveau chemin du dossier personnel (exemple: /home/user): ")

# Variable de la commande qui va être envoyé par paramiko pour créer nouvel utilisateur renseigné
cmd = "sudo usermod --login" " " + str(set_new_user)+" "+ "--home" " " + str(set_new_home)+" " + "--move-home" " " + str(set_user)

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
print("L'utilisateur a bien été renommé et son dossier personnel déplacé !")

