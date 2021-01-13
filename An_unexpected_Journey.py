# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020


@author: BerndKuebrich
"""

#Imports
from map import *                       # Map importieren
from classes import *                   # Klassen importieren
pygame.init()                           # Pygame initalisieren

#Name im Screenhead
pygame.display.set_caption("An unexpected Journey")
clock = pygame.time.Clock()

#Variablen
FPS = 15
GAME_RUNNING = True

# Spielerinstanz erzeugen
classlink = Spielfiguren("Link", 50,50, "top")


# Spielerfigur
link_go_up = [pygame.image.load("sprites/link/link_b0.png"), pygame.image.load("sprites/link/link_b1.png"), pygame.image.load("sprites/link/link_b2.png"), pygame.image.load("sprites/link/link_b3.png"), pygame.image.load("sprites/link/link_b4.png"), pygame.image.load("sprites/link/link_b5.png"), pygame.image.load("sprites/link/link_b6.png"), pygame.image.load("sprites/link/link_b7.png")]
link_go_down = [pygame.image.load("sprites/link/link_f0.png"), pygame.image.load("sprites/link/link_f1.png"), pygame.image.load("sprites/link/link_f2.png"), pygame.image.load("sprites/link/link_f3.png"), pygame.image.load("sprites/link/link_f4.png"), pygame.image.load("sprites/link/link_f5.png"), pygame.image.load("sprites/link/link_f6.png"), pygame.image.load("sprites/link/link_f4.png")]
link_go_left = [pygame.image.load("sprites/link/link_l3.png"), pygame.image.load("sprites/link/link_l1.png"), pygame.image.load("sprites/link/link_l2.png"), pygame.image.load("sprites/link/link_l0.png"), pygame.image.load("sprites/link/link_l4.png"), pygame.image.load("sprites/link/link_l5.png"), pygame.image.load("sprites/link/link_l6.png"), pygame.image.load("sprites/link/link_l7.png")]
link_go_right = [pygame.image.load("sprites/link/link_r0.png"), pygame.image.load("sprites/link/link_r1.png"), pygame.image.load("sprites/link/link_r2.png"), pygame.image.load("sprites/link/link_r3.png"), pygame.image.load("sprites/link/link_r4.png"), pygame.image.load("sprites/link/link_r5.png"), pygame.image.load("sprites/link/link_r6.png"), pygame.image.load("sprites/link/link_r7.png")]
link_frame = 0

#main loop

while GAME_RUNNING:
    # GAME MAP
    for x in range(0, MAPHEIGHT):
        for y in range(0, MAPWIDTH):
            texture = spielfeld[x][y].type
            DISPLAYSURFACE.blit(TEXTURES[texture], (y * TILESIZE, x * TILESIZE))

    #Spielfigur anzeigen
    if classlink.look == "top":
        DISPLAYSURFACE.blit(link_go_up[link_frame], (classlink.rect.left, classlink.rect.top))

    elif classlink.look == "down":
        DISPLAYSURFACE.blit(link_go_down[link_frame], (classlink.rect.left, classlink.rect.top))

    elif classlink.look == "left":
        DISPLAYSURFACE.blit(link_go_left[link_frame], (classlink.rect.left, classlink.rect.top))

    elif classlink.look == "right":
        DISPLAYSURFACE.blit(link_go_right[link_frame], (classlink.rect.left, classlink.rect.top))

    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False


    # Überprüfen, ob Nutzer eine Taste drückt
    buffer = pygame.key.get_pressed()

    if buffer[pygame.K_UP]:
        classlink.look = "top"
        DISPLAYSURFACE.blit(link_go_up[link_frame], (classlink.rect.left, classlink.rect.top))
        if classlink.rect.top >= classlink.speed: #if bedingung damit die figur nicht über den oberen rand hinausgeht
            classlink.tryToMove(0, -1*classlink.speed)

    elif buffer[pygame.K_DOWN]:
        classlink.look = "down"
        DISPLAYSURFACE.blit(link_go_down[link_frame], (classlink.rect.left, classlink.rect.top))
        if classlink.rect.top < (MAPHEIGHT * TILESIZE) -TILESIZE: #if bedingung damit die figur nicht über den unteren rand hinausgeht
            classlink.tryToMove(0, classlink.speed)
            link_frame += 1
            if link_frame > 7:
                link_frame = 0

    elif buffer[pygame.K_RIGHT]:
        classlink.look = "right"
        DISPLAYSURFACE.blit(link_go_right[link_frame], (classlink.rect.left, classlink.rect.top))
        if classlink.rect.left < (MAPWIDTH * TILESIZE) -TILESIZE: #if bedingung damit die figur nicht über den rechten rand hinausgeht
            classlink.tryToMove(classlink.speed, 0)
            link_frame += 1
            if link_frame > 7:
                link_frame = 0

    elif buffer[pygame.K_LEFT]:
        classlink.look = "left"
        DISPLAYSURFACE.blit(link_go_left[link_frame], (classlink.rect.left, classlink.rect.top))
        if classlink.rect.left > 0:         #if bedingung damit die figur nicht über den linken rand hinausgeht
            classlink.tryToMove(-1 * classlink.speed, 0)
            link_frame += 1
            if link_frame > 7:
                link_frame = 0
    else:
        link_frame = 0 #Damit das richtige Spielerbild beim Stehen angezeigt wird

    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






