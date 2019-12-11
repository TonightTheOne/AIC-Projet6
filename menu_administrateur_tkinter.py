#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Steve Petit / Python = 3.6.9 / novembre 2019
# Version 0.1

# Importer les modules nécessaire pour l'exécution du script.
from tkinter import *
from tkinter import ttk 
from xml.dom import minidom
import subprocess
import os

# Définition des actions
def creation_utilisateur_linux():
    subprocess.Popen(["xterm", "-hold", "-sb", "-e", "python3 linux/creation_utilisateur_linux.py"])

def list_user_linux():
    subprocess.Popen(["xterm", "-hold", "-sb", "-e", "python3 linux/lister_utilisateurs_linux.py"])

def modification_utilisateur_linux():
    subprocess.Popen(["xterm", "-hold", "-sb", "-e", "python3 linux/modifier_utilisateur-linux.py"]) 

def backup_home_linux():
    subprocess.Popen(["xterm", "-hold", "-sb", "-e", "python3 linux/backup_home_user.py"]) 
    
def suppression_utilisateur_linux():
    subprocess.Popen(["xterm", "-hold", "-sb", "-e", "python3 linux/suppression_utilisateur_linux.py"]) 


# Définition des fonction scan réseau
def scan_reseau_linux():
    network = input("Entrez l'IP du réseau à scanner (au format IPV4 ex: 192.168.0.0-10): ")
    os.system('xterm -hold -e nmap -PA -sV --version-light' " "  + str(network) + " " '-oX resultat-scan/rapport-scan-linux.xml')
    os.system('grep "\(address\|ostype\)" resultat-scan/rapport-scan-linux.xml | sort -u > resultat/scan/rapport-scan-os.txt')
    os.system('grep -E -o "([0-9]{1,3}[.]){3}[0-9]{1,3}" resultat-scan/rapport-scan-linux.xml | sort -u > resultat-scan/rapport-final-linux.txt')
    print("Scan réseau et trie correctement effectué, inscription des fichier dans /resultat-scan !")

def afficher_resultat_scan_complet():
    fsock=open("resultat-scan/rapport-scan-linux.xml")
    xmldoc = minidom.parse(fsock)
    fsock.close()
    print(xmldoc.toxml())

def afficher_resultat_os_ip():
    fichier_linux=open("resultat-scan/rapport-scan-os.txt", "r")
    for line in fichier_linux:
        print("Voici le résultat IP et OS du scan réseau Linux: ", line)
                         
def afficher_resultat_ip():
    fichier_linux=open("resultat-scan/rapport-final-linux.txt", "r")
    for line in fichier_linux:
        print("Voici le résultat trié des IP du scan réseau Linux: ", line)

# Création et réglages fenêtre
fen=Tk()
fen.title("Automatisation Administrateur Linux")
fen.geometry("1024x800")

# configuration PanedWindow console
pxterm = PanedWindow(fen, orient=VERTICAL)
pxterm.pack(side=LEFT, expand=YES, fill=BOTH, pady=10, padx=10)
pxterm.add(Label(pxterm, text="Console:", background="blue", anchor=CENTER))
pxterm.pack(expand=1)

# Intégration de la console dans le PanelWindows
termf = Frame(pxterm)
termf.pack(side=TOP)
wid = termf.winfo_id()
pxterm.add(termf, minsize=140)
subprocess.Popen('xterm -into %d -geometry 131x500 -hold -sb -e  "tty; sh" &' % wid, shell = True)

# configuration PanedWindow menu
p = PanedWindow(fen, orient=VERTICAL)
p.pack(side=RIGHT, expand=YES, fill=BOTH, pady=10, padx=10)
p.add(Label(p, text='Fonction du script:', background='red', anchor=CENTER))
p.pack()

# Configuration des boutons PanedWindow menu

# bouton pour Scan réseau linux
scan = ttk.Button(p, text='Scan réseau', command=scan_reseau_linux)
scan.pack(side = TOP)
p.add(scan, minsize=65)

# bouton pour Afficher résultat sans trie
result = ttk.Button(p, text='Afficher résultat scan non trié', command=afficher_resultat_scan_complet)
result.pack(side = TOP)
p.add(result, minsize=65)

# bouton pour Afficher résultat IP et OS
ipos = ttk.Button(p, text='Afficher résultat IP et OS', command=afficher_resultat_os_ip)
ipos.pack(side = TOP)
p.add(ipos, minsize=65)

# bouton pour Afficher résultat IP
trie = ttk.Button(p, text='Afficher résultat scan IP', command=afficher_resultat_ip)
trie.pack(side = TOP)
p.add(trie, minsize=65)

# bouton pour Lister utilisateur
listuser = ttk.Button(p, text='Lister les utilisateurs', command=list_user_linux)
listuser.pack(side = TOP)
p.add(listuser, minsize=65)

# bouton pour Création utilisateur
adduser = ttk.Button(p, text='Créer un nouveau utilisateur', command=creation_utilisateur_linux)
adduser.pack(side = TOP)
p.add(adduser, minsize=65)

# bouton pour Mofidier utilisateur
modifyuser = ttk.Button(p, text='Modifier un utilisateur', command=modification_utilisateur_linux)
modifyuser.pack(side = TOP)
p.add(modifyuser, minsize=65)

# bouton pour Sauvegarde répertoire personnel utilisateur
backuphome = ttk.Button(p, text='Sauvegarde des répertoires personnel', command=backup_home_linux)
backuphome.pack(side = TOP)
p.add(backuphome, minsize=65)

# bouton pour Suppression utilisateur
deleteuser = ttk.Button(p, text='Supprimer un utilisateur', command=suppression_utilisateur_linux)
deleteuser.pack(side = TOP)
p.add(deleteuser, minsize=65)

# bouton pour quitter
quitt = ttk.Button(p, text='Quitter', command=fen.destroy)
quitt.pack(side = TOP)
p.add(quitt, minsize=65)

# Pour terminer la boucle avec la souris ou le clavier
fen.mainloop()
