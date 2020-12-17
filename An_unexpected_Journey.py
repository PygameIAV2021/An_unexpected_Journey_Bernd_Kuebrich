# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020


@author: BerndKuebrich
"""
# todo:

from map import *                       # Map importieren
pygame.init()                           # Pygame initalisieren

FPS = 8
GAME_RUNNING = True                       # Konstanten des screens

# set Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (155, 155, 155)

clock = pygame.time.Clock()                         # Uhr initialisiert

class Spielfiguren:
    def __init__(self, name, pos_x, pos_y, speed, look):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 50
        self.look = look

# Spielerinstanz erzeugen
classlink = Spielfiguren("Link", 150, 150, 50, "top")


# Spielfigur
link_go_up = [pygame.image.load("sprites/link/link_b0.png"), pygame.image.load("sprites/link/link_b1.png"), pygame.image.load("sprites/link/link_b2.png"), pygame.image.load("sprites/link/link_b3.png"), pygame.image.load("sprites/link/link_b4.png"), pygame.image.load("sprites/link/link_b5.png"), pygame.image.load("sprites/link/link_b6.png"), pygame.image.load("sprites/link/link_b7.png")]
link_go_down = [pygame.image.load("sprites/link/link_f0.png"), pygame.image.load("sprites/link/link_f1.png"), pygame.image.load("sprites/link/link_f2.png"), pygame.image.load("sprites/link/link_f3.png"), pygame.image.load("sprites/link/link_f4.png"), pygame.image.load("sprites/link/link_f5.png"), pygame.image.load("sprites/link/link_f6.png"), pygame.image.load("sprites/link/link_f4.png")]
link_go_left = [pygame.image.load("sprites/link/link_l3.png"), pygame.image.load("sprites/link/link_l1.png"), pygame.image.load("sprites/link/link_l2.png"), pygame.image.load("sprites/link/link_l0.png"), pygame.image.load("sprites/link/link_l4.png"), pygame.image.load("sprites/link/link_l5.png"), pygame.image.load("sprites/link/link_l6.png"), pygame.image.load("sprites/link/link_l7.png")]
link_go_right = [pygame.image.load("sprites/link/link_r0.png"), pygame.image.load("sprites/link/link_r1.png"), pygame.image.load("sprites/link/link_r2.png"), pygame.image.load("sprites/link/link_r3.png"), pygame.image.load("sprites/link/link_r4.png"), pygame.image.load("sprites/link/link_r5.png"), pygame.image.load("sprites/link/link_r6.png"), pygame.image.load("sprites/link/link_r7.png")]
link_frame = 0


#Bodenerkennung
def getField(x, y):
    map_x = x // TILESIZE
    map_y = y // TILESIZE
    field = MAP1[map_y][map_x]
    return field

maprechteck = pygame.Rect(50, 50, 50, 50)


#main loop
while GAME_RUNNING:
    # GAME MAP
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[MAP1[row][column]], (column * TILESIZE, row * TILESIZE))

    #Spielfigur anzeigen
    if classlink.look == "top":
        DISPLAYSURFACE.blit(link_go_up[link_frame], (classlink.pos_x, classlink.pos_y))

    elif classlink.look == "down":
        DISPLAYSURFACE.blit(link_go_down[link_frame], (classlink.pos_x, classlink.pos_y))

    elif classlink.look == "left":
        DISPLAYSURFACE.blit(link_go_left[link_frame], (classlink.pos_x, classlink.pos_y))

    elif classlink.look == "right":
        DISPLAYSURFACE.blit(link_go_right[link_frame], (classlink.pos_x, classlink.pos_y))

    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False


    # Überprüfen, ob Nutzer eine Taste drückt
    buffer = pygame.key.get_pressed()

    if buffer[pygame.K_UP]:
        classlink.look = "top"
        DISPLAYSURFACE.blit(link_go_up[link_frame], (classlink.pos_x, classlink.pos_y))
        if classlink.pos_y >= TILESIZE: #if bedingung damit die figur nicht über den oberen rand hinausgeht
            if getField(classlink.pos_x, classlink.pos_y - classlink.speed) != WATER:
                classlink.pos_y -= classlink.speed
                link_frame += 1
                if link_frame > 7:
                    link_frame = 0


    elif buffer[pygame.K_DOWN]:
        classlink.look = "down"
        DISPLAYSURFACE.blit(link_go_down[link_frame], (classlink.pos_x, classlink.pos_y))
        if classlink.pos_y < (MAPHEIGHT * TILESIZE) -TILESIZE: #if bedingung damit die figur nicht über den unteren rand hinausgeht
            if getField(classlink.pos_x, classlink.pos_y + classlink.speed) != WATER:
                classlink.pos_y += classlink.speed
                link_frame += 1
                if link_frame > 7:
                    link_frame = 0

    elif buffer[pygame.K_RIGHT]:
        classlink.look = "right"
        DISPLAYSURFACE.blit(link_go_right[link_frame], (classlink.pos_x, classlink.pos_y))
        if classlink.pos_x < (MAPWIDTH * TILESIZE) -TILESIZE: #if bedingung damit die figur nicht über den rechten rand hinausgeht
            if getField(classlink.pos_x + classlink.speed, classlink.pos_y) != WATER:
                classlink.pos_x += classlink.speed
                link_frame += 1
                if link_frame > 7:
                    link_frame = 0

    elif buffer[pygame.K_LEFT]:
        classlink.look = "left"
        DISPLAYSURFACE.blit(link_go_left[link_frame], (classlink.pos_x, classlink.pos_y))
        if classlink.pos_x > 0:         #if bedingung damit die figur nicht über den linken rand hinausgeht
            if getField(classlink.pos_x - classlink.speed, classlink.pos_y) != WATER:
                classlink.pos_x -= classlink.speed
                link_frame += 1
                if link_frame > 7:
                 link_frame = 0
    else:
        link_frame = 0 #Damit das richtige Spielerbild beim Stehen angezeigt wird


    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






