# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020


@author: BerndKuebrich
"""
#todo: Spieler soll beim stehen bleiben die bewegung unterbrechen

from map import *                       #Map importieren
pygame.init()                           #Pygame initalisieren

FPS = 15
GAME_RUNNING = True                       #Konstanten des screens

#set Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (155,155,155)


clock = pygame.time.Clock()                         #Uhr initialisiert
       
#Spielfigur
link_go_up = [pygame.image.load("sprites\link\link_b0.png"), pygame.image.load("sprites\link\link_b1.png"), pygame.image.load("sprites\link\link_b2.png"), pygame.image.load("sprites\link\link_b3.png"), pygame.image.load("sprites\link\link_b4.png"), pygame.image.load("sprites\link\link_b5.png"), pygame.image.load("sprites\link\link_b6.png"), pygame.image.load("sprites\link\link_b7.png")]
link_go_down = [pygame.image.load("sprites\link\link_f0.png"), pygame.image.load("sprites\link\link_f1.png"), pygame.image.load("sprites\link\link_f2.png"), pygame.image.load("sprites\link\link_f3.png"), pygame.image.load("sprites\link\link_f4.png"), pygame.image.load("sprites\link\link_f5.png"), pygame.image.load("sprites\link\link_f6.png"), pygame.image.load("sprites\link\link_f4.png")]
link_go_left = [pygame.image.load("sprites\link\link_l3.png"), pygame.image.load("sprites\link\link_l1.png"), pygame.image.load("sprites\link\link_l2.png"), pygame.image.load("sprites\link\link_l0.png"), pygame.image.load("sprites\link\link_l4.png"), pygame.image.load("sprites\link\link_l5.png"), pygame.image.load("sprites\link\link_l6.png"), pygame.image.load("sprites\link\link_l7.png")]
link_go_right = [pygame.image.load("sprites\link\link_r0.png"), pygame.image.load("sprites\link\link_r1.png"), pygame.image.load("sprites\link\link_r2.png"), pygame.image.load("sprites\link\link_r3.png"), pygame.image.load("sprites\link\link_r4.png"), pygame.image.load("sprites\link\link_r5.png"), pygame.image.load("sprites\link\link_r6.png"), pygame.image.load("sprites\link\link_r7.png")]
link_frame = 0
link_pos_x = 400
link_pos_y = 300
link_speed = 10
link_look_direction = "top"

def check_water(x,y):
    map_x = x // TILESIZE
    map_y = y // TILESIZE
    field = MAP1[map_x][map_y]
    print("BLUBB",field)
    return field == WATER


#main loop
while GAME_RUNNING:
    # GAME MAP
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[MAP1[row][column]], (column * TILESIZE, row * TILESIZE))

    #Spielfigur anzeigen
    if link_look_direction == "top":
        DISPLAYSURFACE.blit(link_go_up[link_frame], (link_pos_x, link_pos_y))

    elif link_look_direction == "down":
        DISPLAYSURFACE.blit(link_go_down[link_frame], (link_pos_x, link_pos_y))

    elif link_look_direction == "left":
        DISPLAYSURFACE.blit(link_go_left[link_frame], (link_pos_x, link_pos_y))

    elif link_look_direction == "right":
        DISPLAYSURFACE.blit(link_go_right[link_frame], (link_pos_x, link_pos_y))

    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            GAME_RUNNING = False


    # Überprüfen, ob Nutzer eine Taste drückt
    buffer = pygame.key.get_pressed()
    if buffer[pygame.K_UP]:
        link_look_direction = "top"
        DISPLAYSURFACE.blit(link_go_up[link_frame], (link_pos_x, link_pos_y))
        if link_pos_y > MAPHEIGHT: #if bedingung damit die figur nicht über den oberen rand hinausgeht
            if not check_water(link_pos_x, link_pos_y - link_speed):
                link_pos_y -= link_speed
                link_frame += 1
                if link_frame > 7:
                    link_frame = 0


    elif buffer[pygame.K_DOWN]:
        link_look_direction = "down"
        DISPLAYSURFACE.blit(link_go_down[link_frame], (link_pos_x, link_pos_y))
        if link_pos_y < (MAPHEIGHT * TILESIZE) -TILESIZE: #if bedingung damit die figur nicht über den unteren rand hinausgeht
            if not check_water(link_pos_x, link_pos_y + link_speed):
                link_pos_y += link_speed
                link_frame += 1
                if link_frame > 7:
                    link_frame = 0

    elif buffer[pygame.K_RIGHT]:
        link_look_direction = "right"
        DISPLAYSURFACE.blit(link_go_right[link_frame], (link_pos_x, link_pos_y))
        if link_pos_x < (MAPWIDTH * TILESIZE) -TILESIZE: #if bedingung damit die figur nicht über den rechten rand hinausgeht
            if not check_water(link_pos_x + link_speed, link_pos_y ):
                link_pos_x += link_speed
                link_frame += 1
                if link_frame > 7:
                    link_frame = 0

    elif buffer[pygame.K_LEFT]:
        link_look_direction = "left"
        DISPLAYSURFACE.blit(link_go_left[link_frame], (link_pos_x, link_pos_y))
        if link_pos_x > 0:         #if bedingung damit die figur nicht über den linken rand hinausgeht
            if not check_water(link_pos_x  - link_speed, link_pos_y):
                link_pos_x -= link_speed
                link_frame += 1
                if link_frame > 7:
                 link_frame = 0
    else:
        link_frame = 0 #Damit das richtige Spielerbild beim Stehen angezeigt wird


    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)  

pygame.quit()          
  





