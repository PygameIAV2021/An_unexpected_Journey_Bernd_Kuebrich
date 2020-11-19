# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020

@author: BerndKuebrich
"""

import pygame                           #Pygame importieren
pygame.init()                           #Pygame initalisieren

WIDHT, HEIGHT, FPS = 800, 600, 60                #Konstanten des screens

#Farben setzen
BLACK = (0,0,0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDHT, HEIGHT)) #Screen definieren
pygame.display.set_caption("An unexpected Journey") #Name im Screenhead
clock = pygame.time.Clock()                         #Uhr initialisiert

#main loop
while True:
    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        #Beenden bei "ESC"
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            
    #Spiellogik
    
    #Spielfeld löschen
    screen.fill(WHITE)

    #Spielfeld/Spielfiguren

    #Screen aktualisieren
    pygame.display.flip()
    clock.tick(FPS)            
            





