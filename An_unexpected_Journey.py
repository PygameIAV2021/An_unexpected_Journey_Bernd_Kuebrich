# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020

@author: BerndKuebrich
"""

#Imports
from map import *                       # Map importieren
from classes import *                   # Klassen importieren

pygame.init()
clock = pygame.time.Clock()

#Name im Screenhead
pygame.display.set_caption("An unexpected Journey")

#Variablen
FPS = 15
GAME_RUNNING = True

#Spielerinstanz erzeugen
classlink = Spielfiguren("Link", 50,300, "down")

#main loop
while GAME_RUNNING:

    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False

    #Überprüfen, ob Nutzer eine Taste drückt
    buffer = pygame.key.get_pressed()

    #Bewegung nach Oben
    if buffer[pygame.K_UP]:
        move = classlink.tryToMove("up")
    #Bewegung nach Unten
    elif buffer[pygame.K_DOWN]:
        classlink.tryToMove("down")
    #Bewegung nach Rechts
    elif buffer[pygame.K_RIGHT]:
        classlink.tryToMove("right")
    #Bewegung nach Links
    elif buffer[pygame.K_LEFT]:
        classlink.tryToMove("left")
    else:
        classlink.spritecounter = 0 #Damit das richtige Spielerbild beim Stehen angezeigt wird

    # GAME MAP
    for x in range(0, MAPHEIGHT):
        for y in range(0, MAPWIDTH):
            texture = spielfeld[x][y].type
            DISPLAYSURFACE.blit(TEXTURES[texture], (y * TILESIZE, x * TILESIZE))

    classlink.draw()
    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






