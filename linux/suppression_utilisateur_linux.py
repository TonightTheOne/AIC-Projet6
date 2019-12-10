#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paramiko

# Variable pour la connexion SSH
hostname = input("Entrez adresse IP pour la connexion SSH: ")
username = input("Entrez utilisateur: ")
keyrsa = "/home/steve/.ssh/id_rsa.pub" # Modifier avec votre chemin

# Variable pour l'utilisateur à supprimer
user_del=input("Entrez nom utilisateur à supprimer: ")

# Initialise la connexion SSH
client = paramiko.SSHClient()

# Ajoutes les hosts connus
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, key_filename=keyrsa)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# Variable de la commande qui va être envoyé par paramiko
cmd = "sudo userdel -f -r " + str(user_del)

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
print("L'utilisateur a bien été supprimé")
