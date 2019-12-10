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

# Variable pour l'utilisateur à créer
user_add=input("Entrez le nom de l'utilisateur à créer: ")

# Variable pour récupérer le nom d'utilisateur créer pour le changement de mot de passe au premier boot
user_modify_pass = user_add

# Variable pour le mot de passe du nouveau utilisateur
user_pass=getpass("Entrez le mot de passe pour le nouveau utilisateur: ")
encPass = crypt.crypt(user_pass,"22")

# Initialise la connexion SSH
client = paramiko.SSHClient()

# Ajoutes les hosts connus
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# Variable de la commande qui va être envoyé par paramiko pour créer nouvel utilisateur renseigné
cmd = "sudo useradd --create-home  --password " + str(encPass) +" "+ str(user_add)

# Exécution de la commande 
stdin, stdout, stderr = client.exec_command(cmd)

# Lire la sortie standard et l'afficher
print(stdout.read().decode())

# Variable de la commande envoyé par paramiko pour que l'utilisateur modifie son mot de passe à la première connexion
cmd2 = "sudo passwd -e " + str(user_modify_pass)

# Exécution de la commande 
stdin, stdout, stderr = client.exec_command(cmd2)

# Lire la sortie standard et l'afficher
print(stdout.read().decode())

# Affiche les erreurs si il y en a
err = stderr.read().decode()
if err:
    print(err)
    
# Ferme la connexion
client.close()
print("L'utilisateur a bien été créé !")
