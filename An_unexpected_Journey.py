# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020

@author: BerndKuebrich
"""

#Imports
from classes import pygame, Player, Sword, Shield, Ganon, Bow
from map import levelHolder, Map, DISPLAYSURFACE, MAPHEIGHT, TILESIZE
from game import Game
import sys
from os import path
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#COLORS
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
GREEN = (60, 179, 113)
RED = (178, 0, 0)

#Konstanten
FPS = 20
GAME_RUNNING = True
LEVEL = 0
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)

#Variablen
currentMap = Map(levelHolder[LEVEL].map) # type: Map
music = path.join(path.dirname(__file__), 'Music')


#Instanzen erzeugen
player_instance = Player("Link", levelHolder[LEVEL].startPosition, "down", currentMap)
sword_instance = Sword()
shield_instance = Shield()
ganon = Ganon()
bow_instance = Bow()
menu = Game()
menu.running = True

#Name im Screenhead
pygame.display.set_caption("An unexpected Journey")

#Musik
#pygame.mixer.music.load(path.join(music, 'mainmusic.mp3'))
#pygame.mixer.music.set_volume(0.4)
#pygame.mixer.music.play(loops = -1)

#Aufsammelbare Items
GAME_ITEMS = [sword_instance, shield_instance, bow_instance]

#Funktionen
def pickupitems(item_instance, x, y):
    for item in GAME_ITEMS:
        if player_instance.rect.left in range(x, y) and player_instance.rect.top in range(x, y) and item.placed:
            item_instance.placed = False
    return

#Menü Loop
while menu.running:

    menu.curr_menu.display_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
    menu.running = False

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

    #Spieler-Lebensleiste anzeigen
    player_health_bar_text = HEALTHFONT.render('LINK HEALTH:', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(player_health_bar_text, (15, MAPHEIGHT * TILESIZE - 700))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(player_instance.health), True, GREEN, BLACK), (225, MAPHEIGHT * TILESIZE - 700))

    #Items anzeigen
    for item in GAME_ITEMS:
        if item.placed == True and LEVEL == 0:
            DISPLAYSURFACE.blit(item.image, (item.pos[0], item.pos[1]))
        else:
            DISPLAYSURFACE.blit(pygame.transform.scale(item.image, (40, 40)), (item.inventory_pos[0], item.inventory_pos[1]))

    # Items aufheben
    pickupitems(sword_instance, 475, 525)
    pickupitems(shield_instance, 225,275)
    pickupitems(bow_instance, 375, 425)

    #Ganon plus Ganon-Lebensleiste anzeigen
    if LEVEL == 2:
        ganon_healthbar_text = HEALTHFONT.render('GANON HEALTH:', RED, BLACK)
        DISPLAYSURFACE.blit(ganon_healthbar_text, (650, MAPHEIGHT * TILESIZE - 700))
        DISPLAYSURFACE.blit(HEALTHFONT.render(str(ganon.Health), RED, BLACK), (900, MAPHEIGHT * TILESIZE - 700))
        DISPLAYSURFACE.blit(ganon.Ganon, (850, MAPHEIGHT * TILESIZE - 400))

    player_instance.draw()

    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






