# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:29:35 2020

@author: BerndKuebrich
"""
import pygame

# TILES
DIRT = 0
GRASS = 1
WATER = 2
WALL = 3

#Game dimensions
TILESIZE = 50


#Dictionary linking tiles to their colors

TEXTURES = {
    DIRT: pygame.transform.scale(pygame.image.load('Level/ground.png'), (TILESIZE, TILESIZE)),
    GRASS: pygame.transform.scale(pygame.image.load('Level/grass.png'), (TILESIZE, TILESIZE)),
    WATER: pygame.transform.scale(pygame.image.load('Level/water.png'), (TILESIZE, TILESIZE)),
    WALL: pygame.transform.scale(pygame.image.load('Level/wall.png'),   (TILESIZE, TILESIZE))
}

#Tiles to be displayed
MAP1= [
   [WATER, GRASS, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
   [WATER, GRASS, DIRT, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
]

MAPWIDTH = len(MAP1[0])
MAPHEIGHT = len(MAP1)

pygame.init()
pygame.display.set_caption("An unexpected Journey") #Name im Screenhead
#MAP
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

#COLORS
WHITE = (200,200,200)
BLACK = (0,0,0)
BLUE = (30,144,255)
GREEN = (60,179,113)
RED = (178,0,0)


