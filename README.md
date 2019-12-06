__________________________________________________________________
# Parcours OpenClassRooms Administrateur Infrastructure et Cloud #
__________________________________________________________________

__________________________________________________________________
# Projet 6 : Participez à la vie de la communauté Open Source    #
__________________________________________________________________

__________________________________________________________________
# Auteur : Steve Petit                                           #
# Date de création : novembre 2019                               #
# Dernière modification : 5 décembre 2019                        #
# Version de Python : 3.7.3                                      #
__________________________________________________________________

__________________________________________________________________
# Prérequis                                                      #
__________________________________________________________________

# Python  
  
Version recommandée : 3.7.3 (32 ou 64 bits)  
Le langage Python est disponible au téléchargement à l’adresse suivante : https://www.python.org/downloads/  
  
# Modules utilisés  
  
tkinter  
Paramiko  
subprocess  
os  
getpass  
crypt  
   
# Configuration des machines cibles  

Pour des raisons de simplicité, les machines cibles doivent êtres configurées pour autoriser l'authentification SSH.  
  
_________________________________________________________________
# Démarrage du script                                           #
_________________________________________________________________
  
  
Se placer dans le repértoire contenant le script "menu_administrateur_tkinter.py" avec cd ou en lancant le terminal directement dans le dossier, ensuite lancer le script avec cette commande :  
  
$  python3 menu_administrateur_tkinter.py  
  
_________________________________________________________________
# Utilisation                                                   #
_________________________________________________________________
  
La GUI se présente sous la forme d'une fenêtre divisé en deux sections :  
  
![ScreenShot](https://github.com/TonightTheOne/AIC-Projet6/blob/master/documentation/menu.PNG)  
  
Menu de gauche :  
- Terminal interne pour test en même temps que éxecution des scripts  
  
Menu de droite :  
- Scan réseau NMAP et détection de l'OS avec inscription résultat dans fichier .xml à l'intérieur dossier /resultat-scan  
- Grep sur fichier .xml pour récupérer les adresses IP des machines du réseau avec inscription dans .txt -> /resultat-scan 
   - répertoire resultat-scan :  
      - Répertoire de reception du .xml scan NMAP  
      - Répertoire de réception du .txt trie IP  
- Script pour lister utilisateurs de la machine ciblé, connexion SSH avec paramiko  
- Script création utilisateur et modification passe au premier Login sur machine ciblé, connexion SSH avec paramiko  
- Script modification nom utilisateur et son home sur la machine ciblé, connexion SSH avec paramiko  
- Script sauvegarde des dossiers home de la machine ciblé, connexion SSH avec paramiko, sauvegarde avec rsync  
- Script suppresion utilisateur sur la machine ciblé, suppresion du home inclus, connexion SSH avec paramiko   


      
   - répertoire resultat-scan :  
      - Répertoire de reception du .xml scan NMAP  
      - Répertoire de réception du .txt trie IP  
      
__________________________________________________________________
# Execution du script                                            #
__________________________________________________________________
  
Les scripts sont interactif, ils vont demander les informations avant de lancer les commandes.  
  
Scan réseau :  

- Pour le scan réseau, l'IP réseau et sa plage à scanner se fera dans le terminal de lancement du scrypt :  
  
![ScreenShot](https://github.com/TonightTheOne/AIC-Projet6/blob/master/documentation/scan-réseau-lancement.PNG)  
  
- La commande est éxecuter dans subprocess xterm et le résultat enregistré dans le repertoire resultat-scan/ en fichier .xml  
  
![ScreenShot](https://github.com/TonightTheOne/AIC-Projet6/blob/master/documentation/scan-réseau-execution.PNG)  
  


      
