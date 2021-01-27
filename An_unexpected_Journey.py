# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020

@author: BerndKuebrich
"""

#Imports
from classes import pygame, Player, Sword
from map import levelHolder, Map, DISPLAYSURFACE, MAPHEIGHT, TILESIZE

pygame.init()
clock = pygame.time.Clock()

#COLORS
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
GREEN = (60, 179, 113)
RED = (178, 0, 0)

#Name im Screenhead
pygame.display.set_caption("An unexpected Journey")

#Konstanten
FPS = 15
GAME_RUNNING = True
LEVEL = 0
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)
INVENTORYFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)

#Variablen
currentMap = Map(levelHolder[LEVEL].map) # type: Map

#Instanzen erzeugen
player_instance = Player("Link", levelHolder[LEVEL].startPosition, "down", currentMap)
sword_instance = Sword()

#Benötigte Listen
GAME_ITEMS = [sword_instance]




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
        move = player_instance.tryToMove("up")
    #Bewegung nach Unten
    elif buffer[pygame.K_DOWN]:
        player_instance.tryToMove("down")
    #Bewegung nach Rechts
    elif buffer[pygame.K_RIGHT]:
        player_instance.tryToMove("right")
    #Bewegung nach Links
    elif buffer[pygame.K_LEFT]:
        player_instance.tryToMove("left")
    else:
        player_instance.spritecounter = 0 #Damit das richtige Spielerbild beim Stehen angezeigt wird

    #Level/Map Wechsel
    changeLevel = levelHolder[LEVEL].isOnChangePosition(player_instance)
    if changeLevel == 'next':
        LEVEL += 1
        currentMap = Map(levelHolder[LEVEL].map)  # type: Map
        player_instance.changeLevel(levelHolder[LEVEL].startPosition, currentMap)
    elif changeLevel == 'previous':
        LEVEL -= 1
        currentMap = Map(levelHolder[LEVEL].map)  # type: Map
        player_instance.changeLevel(levelHolder[LEVEL].previousPosition, currentMap)
    currentMap.draw()

    #Level/Map Wechsel Rechtecke anzeigen
    # if levelHolder[level].nextLevelRect is not None:
    #     for rect in levelHolder[level].nextLevelRect: #type: pygame.Rect
    #         pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), rect)
    # if levelHolder[level].previousLevelRect is not None:
    #     for rect in levelHolder[level].previousLevelRect:  # type: pygame.Rect
    #         pygame.draw.rect(DISPLAYSURFACE, (0, 0, 255), rect)

    #Lebensleiste anzeigen
    PLAYER_HEALTH_BAR_TEXT = HEALTHFONT.render('LINK HEALTH:', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(PLAYER_HEALTH_BAR_TEXT, (15, MAPHEIGHT * TILESIZE - 700))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(player_instance.health), True, GREEN, BLACK), (225, MAPHEIGHT * TILESIZE - 700))

    ##Spielerinventar anzeigen
    #INVENTORY_POSITION = 250
    #for item in player_instance.inventory:
    #    DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT * TILESIZE + 35))
    #    INVENTORY_POSITION += 10
    #    INVENTORY_TEXT = INVENTORYFONT.render(item.NAME, True, WHITE, BLACK)
    #    DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT * TILESIZE + 15))
    #    INVENTORY_POSITION += 100

    #Items anzeigen
    for item in GAME_ITEMS:
        if item.PLACED == True and LEVEL == 0:
            DISPLAYSURFACE.blit(item.IMAGE, (item.POS[0], item.POS[1]))

    #Items aufheben
    #for item in GAME_ITEMS:
    #    if player_instance.PLAYER_POS == item.POS and item.PLACED:
    #       player_instance.inventory.append(item)
    #       item.PLACED = False
    #       if item in GAME_WEAPONS:
    #            PLAYER.WEAPON = item



    player_instance.draw()
    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






