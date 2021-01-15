# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020

@author: BerndKuebrich
"""

#Imports
from classes import pygame, Spielfiguren
from map import levelHolder, Map, DISPLAYSURFACE

pygame.init()
clock = pygame.time.Clock()

#Name im Screenhead
pygame.display.set_caption("An unexpected Journey")

#Variablen
FPS = 15
GAME_RUNNING = True
level = 0

currentMap = Map(levelHolder[level].map) # type: Map
#Spielerinstanz erzeugen
classlink = Spielfiguren("Link", levelHolder[level].startPosition, "down", currentMap)

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

    changeLevel = levelHolder[level].isOnChangePosition(classlink)
    if changeLevel == 'next':
        level += 1
        currentMap = Map(levelHolder[level].map)  # type: Map
        classlink.changeLevel(levelHolder[level].startPosition, currentMap)
    elif changeLevel == 'previous':
        level -= 1
        currentMap = Map(levelHolder[level].map)  # type: Map
        classlink.changeLevel(levelHolder[level].previousPosition, currentMap)
    currentMap.draw()

    # if levelHolder[level].nextLevelRect is not None:
    #     for rect in levelHolder[level].nextLevelRect: #type: pygame.Rect
    #         pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), rect)
    # if levelHolder[level].previousLevelRect is not None:
    #     for rect in levelHolder[level].previousLevelRect:  # type: pygame.Rect
    #         pygame.draw.rect(DISPLAYSURFACE, (0, 0, 255), rect)

    classlink.draw()
    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






