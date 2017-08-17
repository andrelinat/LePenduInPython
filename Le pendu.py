# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" LE JEU DU PENDU. Script écrit avec Python 3.4.0 et Pygame 1.9.2a0-py3.4
par André LINAT """

import sys
import time
import pygame
from random import *
from pygame.locals import *

pygame.init()


# Ouverture du fichier contenant les mots en mode lecture.

fichier = open("Dico.dat", "r")
liste_mots = fichier.readlines()
fichier.close()

# Lecture de tous les mots du fichier dans une liste.

def lettre_dans_mot(lettre):
    global partie_en_cours, mot_partiel, mot_choisi, nb_echecs
    global son_perdu, son_gagne
    if partie_en_cours : 
        nouveau_mot_partiel = ""
        lettre_dans_mot = False # Faux.
        i=0
        while i<len(mot_choisi):
            if mot_choisi[i]==lettre:
                nouveau_mot_partiel = nouveau_mot_partiel + lettre
                lettre_dans_mot = True # Vrai. 
            else:
                nouveau_mot_partiel = nouveau_mot_partiel + mot_partiel[i]
            i+=1
        mot_partiel = nouveau_mot_partiel  
        afficher_mot(mot_partiel)
        if not lettre_dans_mot:        # Lettre eronnée. Changement image.
            nb_echecs += 1
            nomFichier = "Images/Potence_"+str(nb_echecs)+".jpg"
            if nb_echecs == 10:  	# Les lettres n'ont pas été trouvées. Pendaison.
                partie_en_cours = False # Faux.
                afficher_mot(mot_choisi)
                son_perdu.play()
        elif mot_partiel == mot_choisi:  # Le mot a été trouvé.
            partie_en_cours = False # Faux.
            son_gagne.play()

# Déclarations globales.
global image_prenom, fenetre, police

# Initialisation Pygame.
pygame.init()

# Initialisation de l'horloge du jeu.
framerate = pygame.time.Clock()

# Création de la fenêtre principale.
largeur = 1024
hauteur = 768

# Affichage écran de bienvenue.
fenetre = pygame.display.set_mode((largeur, hauteur)) # FULLSCREEN pour plein écran.

# Effacement du curseur
pygame.mouse.set_visible(0) # 0 = Invisible 1 = Visible

# Chargement et collage du fond
presentation = pygame.image.load("Images/Generique.jpg").convert()
fenetre.blit(presentation, (0, 0))

# Collage de l'icone
global image_icone
image_icone = "Images/Icone.png"
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

# Titre de la fenêtre.
global titre_jeu
titre_jeu = "Le jeu du Pendu par André LINAT® 2016"
pygame.display.set_caption(titre_jeu)
pygame.display.flip()

# Boucle attente.
pygame.time.delay (1000) # En millisecondes.

# Affichage du parchemin "Prénom".
image_prenom = pygame.image.load("Images/Prenom.png").convert_alpha()
fenetre.blit(image_prenom, (218, 460))

# Rafraîchissement image.
pygame.display.flip()

# Affichage étoile sherif.
pygame.time.delay (500) # En millisecondes.
etoile = pygame.image.load("Images/Etoile_2.png").convert_alpha()
fenetre.blit(etoile, (260, 570))

# Rafraîchissement  de l'image.
pygame.display.flip()
               
# Police pour le prénom du joueur.
police = pygame.font.Font("Font/JesterRES.ttf", 42, bold = False, italic = False)

# Ecrire et afficher le prénom du joueur.
nom_joueur = ""

# Boucle attente saisie du prénom du joueur.
patronyme = 1

while patronyme:
    # Attente saisie du prénom du joueur.
    for event in pygame.event.get():
        if event.type == QUIT:
            patronyme = 0
            """ Gestion des touches du clavier pour entrer le prénom du joueur"""
            # Appuie sur la touche "Return" pour valider le prénom.
        elif event.type == KEYDOWN and event.key == pygame.K_RETURN: 
            patronyme = 0
            # Appuie sur la touche "Entrée" clavier numérique pour valider le prénom.
        elif event.type == KEYDOWN and event.key == pygame.K_KP_ENTER:    
            patronyme = 0
            # Appuie dur la touche "Backspace" pour effacer le dernier caractère.
        elif event.type == KEYDOWN and event.key == pygame.K_BACKSPACE:
            nom_joueur = nom_joueur = caractere
            print (nom_joueur)
            # Appuie sur une touche quelconque.       
        elif event.type == KEYDOWN:
            caractere = event.dict['unicode']
            nom_joueur = nom_joueur + caractere
            print(nom_joueur)
            # Met la première lettre en capitale.
            nom_joueur = nom_joueur.capitalize()
            """ Couleur des police du prénom joueur """           
            # Couleur du dessous présentation du joueur "Noire".
            text = police.render(nom_joueur, 1, (0, 0, 0))
            # Récupération du rectangle de cette surface.
            textRect = text.get_rect()
            # Positionnement du rectangle texte Noir.
            textRect.x = 313 
            textRect.y = 563
            # Affichage du texte Noir.
            fenetre.blit(text, textRect)
            # Couleur du dessus présentation du joueur "Vert".
            text = police.render(nom_joueur, 1, (0, 128, 0))
            # Récupération du rectangle de cette surface.
            textRect = text.get_rect()
            # Positionnement du rectangle texte Vert.
            textRect.x = 310 
            textRect.y = 560
            # Affichage du texte Vert.
            fenetre.blit(text, textRect)            
            # Rafraîchissement de l'image.
            pygame.display.update()
            
        elif event.type == KEYDOWN and event.key == pygame.K_RETURN:
            patronyme = 0
              
        else:
            continue

# Ouverture du fichier "Patronyme" en écriture.
fichier = open("Patronyme.dat", "w")
fichier.write(nom_joueur)
fichier.close()

# Ouverture du fichier "Champion" en écriture.
fichier = open("Champion.dat", "w")
fichier.write(nom_joueur)
fichier.close() 
    

# Attente pour affichage suivant.
pygame.time.delay(100) # En millisecondes.

# Affichage du parchemin "Les règles".
image_prenom = pygame.image.load("Images/Les_regles.png").convert_alpha()
fenetre.blit(image_prenom, (218, 460))
police = pygame.font.Font("Font/JesterRES.ttf", 32, bold=False, italic=False)
# Couleur du dessous présentation du joueur "Rouge".
text = police.render(nom_joueur, 1, (255, 0, 0))
# Récupération du rectangle de cette surface.
textRect =text.get_rect()
# Positionnement du rectangle texte Rouge.
textRect.centerx = fenetre.get_rect().centerx+2
textRect.y = 497
# Affichage du texte Noir.
fenetre.blit(text, textRect)
# Couleur du dessus présentation du joueur "Bleu".
text = police.render(nom_joueur, 1, (0, 0, 192))
# Récupération du rectangle de cette surface.
textRect =text.get_rect()
# Positionnement du rectangle texte Bleu.
textRect.centerx = fenetre.get_rect().centerx
textRect.y = 495
# Affichage du texte Vert.
fenetre.blit(text, textRect)

# Rafraîchissement de l'image.
pygame.display.flip()

# Boucle attente saisie des règles du jeu.
voir_regles_jeu = True

while voir_regles_jeu:

    # Attente saisie décision du joueur.
    for event in pygame.event.get():
        if event.type == QUIT:
            
            voir_regles_jeu = False
            
        # Touche voir règles = "F2".
        elif event.type == KEYDOWN and event.key == pygame.K_F2:
            image_regles = pygame.image.load("Images/Regles_pendu.jpg").convert()
            fenetre.blit(image_regles, (0, 0))
            pygame.display.flip()
            
            voir_regles_jeu = True
                      
        
        # Touche suite = "Espace".
        elif event.type == KEYDOWN and event.key == pygame.K_SPACE:
            tableau_honneur = pygame.image.load("Images/Tableau_honneur.jpg").convert()
            fenetre.blit(tableau_honneur, (0, 0))
            pygame.display.flip()
            
            voir_regles_jeu = True
           
                
        # Touche jouer = "F5".
        elif event.type ==KEYDOWN and event.key == pygame.K_F5:
            debut_jeu = pygame.image.load("Images/Potence_0.jpg").convert()
            fenetre.blit(debut_jeu, (0, 0))
            pygame.display.flip()
            
            voir_regles_jeu = False
                    
            
        # Touche quitter = "F7".                
        elif event.type ==KEYDOWN and event.key == pygame.K_F7:
            fin_partie = pygame.image.load("Images/Fin_partie.jpg").convert()
            fenetre.blit(fin_partie, (0, 0))
            pygame.display.flip()
            pygame.time.delay(1000) # En millisecondes.
            
            voir_regles_jeu = False
                      
                            

        
        
def nom_du_champion():
        
    # Position du nom du champion.
    police = pygame.font.Font("Font/PlayBill.ttf", 52, bold=False, italic=False)

    """ Affichage du nom du jouer ayant le meilleur score."""
        
    # Couleur du dessous nom du champion "Noir".
    text = police.render(nom_joueur, 1, (0, 0, 0))
    
    # Récupération du rectangle de cette surface.
    textRect = text.get_rect()
    # Positionnement du rectangle texte Noir (63, 129).
    textRect.centerx = fenetre.get_rect().centerx-336 # Ici le texte "Noir" est centré
    textRect.y = 135                                  # sur la fenêtre "Le champion".
    fenetre.blit(text, textRect)        
                
    # Couleur du dessus présentation du joueur "Rouge".
    text = police.render(nom_joueur, 1, (255, 0, 0))

    # Récupération du rectangle de cette surface.
    textRect = text.get_rect()
    # Positionnement du rectangle texte Rouge (60, 126).
    textRect.centerx = fenetre.get_rect().centerx-338 # Ici le texte "Rouge" est centré
    textRect.y = 132                                  # sur la fenêtre "Le champion".
    fenetre.blit(text, textRect)
    
    # Rafraîchissement de l'écran.
    pygame.display.flip()

                    


# Affichage du personnage gagnant.


# Jouer son quand le joueur perd.
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
son_perdu = pygame.mixer.Sound("Sons/PacMan.wav")
son_perdu.stop()

# Jouer son quand le joueur gagne.
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
son_gagne = pygame.mixer.Sound("Sons/Tada.wav")
son_gagne.stop()

# Affichage du mot.
def afficher_mot():
    global mot, lettres
    mot = ""
    mot_large = ""
    i = 0
    
    # Ajout d'un espace entre les lettres du mot.
    while i<len(mot):  
        mot_large = mot_large + mot[i] + " "
        i += 1
        
        police = pygame.font.Font("Font/JesterRES.ttf", 30, bold=False, italic=False)
        lettres = police.render(mot_partiel, 1, (0, 0, 0)) # Couleur Noire.
        
        # Ici le mot à trouver est centré sur la fenêtre "Le mot".
        textRect = text.get_rect()
        textRect.centerx = fenetre.get_rect().centerx+246
        textRect.y = 92
                    
        # Position du futur mot à trouver.
        fenetre.blit(lettres, textRect)
                        
        # Rafraîchissement de l'écran.
        pygame.display.flip()
 

# Proposition d'une letrre.


        
# Initialisation du jeu.
    
def init_jeu():
    
    global nb_echecs, partie_en_cours, mot_choisi, afficher_mot
    global mot_partiel, nom_du_champion, lettre_dans_mot
    global liste_mots
    
    nb_echecs = 0
    partie_en_cours = True
    mot_choisi = choice(liste_mots).rstrip()
    mot_choisi = mot_choisi.upper() # Mise en majuscules du mot.
    mot_partiel = "-" * len(mot_choisi)
    afficher_mot()
    nom_du_champion()
    lettre_dans_mot()

def recommencer_jeu():
                 
    global image_pendu
                 
    image_pendu = pygame.image.load("Images/Potence_0.jpg").convert()
    fenetre.blit(image_pendu, (0, 0))
    pygame.display.flip()


# Début partie.
init_jeu()


# Vidage de la pile d'évènements.
boucle = 1

while boucle:
    # Attente saisie pour quitter le programme.
    for event in pygame.event.get():
        if event.type == QUIT:
            boucle = 0
            
        # Touche rejouer = "F3".
        elif event.type ==KEYDOWN and event.key == pygame.K_F3:
            debut_jeu = pygame.image.load("Images/Potence_0.jpg").convert()
            fenetre.blit(debut_jeu, (0, 0))
            pygame.display.flip()
            boucle = 1            
        
            
# Attente pour affichage suivant..
# pygame.time.delay(3000) # En millisecondes.

pygame.quit()
