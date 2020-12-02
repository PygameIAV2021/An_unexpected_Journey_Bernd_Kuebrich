# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:32:48 2020

@author: BerndKuebrich
"""

import pygame                           #Pygame importieren
from map import *
pygame.init()                           #Pygame initalisieren

WIDHT, HEIGHT, FPS = 500, 500, 10
GAME_RUNNING = True                       #Konstanten des screens

#set Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (155,155,155)


clock = pygame.time.Clock()                         #Uhr initialisiert
       
#Spielfigur
#player_character = pygame.image.load("round_ghost/round_ghost_idle/sprite_0.png")
#picture_size = player_character.get_rect()
ghost = [pygame.image.load("round_ghost/round_ghost_walk/sprite_0.png"),pygame.image.load("round_ghost/round_ghost_walk/sprite_1.png"),pygame.image.load("round_ghost/round_ghost_walk/sprite_2.png"),pygame.image.load("round_ghost/round_ghost_walk/sprite_3.png"),pygame.image.load("round_ghost/round_ghost_walk/sprite_4.png"),pygame.image.load("round_ghost/round_ghost_walk/sprite_5.png")]
ghost_frame = 0
ghost_pos_x = 400
ghost_pos_y = 300
ghost_speed = 15
#main loop
while GAME_RUNNING:
    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            GAME_RUNNING = False
    #Spielfigur Steuerung        
    buffer = pygame.key.get_pressed()
    if buffer[pygame.K_UP]:
        ghost_pos_y -= ghost_speed
    elif buffer[pygame.K_DOWN]:
        ghost_pos_y += ghost_speed
    elif buffer[pygame.K_RIGHT]:
        ghost_pos_x += ghost_speed  
    elif buffer[pygame.K_LEFT]:
        ghost_pos_x -= ghost_speed  
        
            
    #GAME MAP
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[MAP1[row][column]], (column*TILESIZE, row*TILESIZE))        
    
          
    
    #Spiellogik
    
    #Spielfeld löschen nach jedem FPS
    

    #Spielfeld/Spielfiguren
    ghost_frame +=1
    if ghost_frame > 5:
        ghost_frame = 0
    DISPLAYSURFACE.blit(ghost[ghost_frame], (ghost_pos_x,ghost_pos_y))
    
    #Screen aktualisieren
    pygame.display.update()
    clock.tick(FPS)  

pygame.quit()          
  





