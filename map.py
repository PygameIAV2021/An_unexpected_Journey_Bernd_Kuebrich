# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:29:35 2020

@author: BerndKuebrich
"""
import pygame
import enum

# TILES
class Tiles(enum.Enum):
    DIRT = 0
    GRASS = 1
    WATER = 2
    WALL = 3

#Game dimensions
TILESIZE = 50

#Dictionary linking tiles to their colors
TEXTURES = {
    Tiles.DIRT: pygame.transform.scale(pygame.image.load('Level/ground.png'), (TILESIZE, TILESIZE)),
    Tiles.GRASS: pygame.transform.scale(pygame.image.load('Level/grass.png'), (TILESIZE, TILESIZE)),
    Tiles.WATER: pygame.transform.scale(pygame.image.load('Level/water.png'), (TILESIZE, TILESIZE)),
    Tiles.WALL: pygame.transform.scale(pygame.image.load('Level/wall.png'),   (TILESIZE, TILESIZE))
}

#Tiles to be displayed
MAP1= [
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.WATER, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
[Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
[Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
[Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
[Tiles.WATER, Tiles.GRASS, Tiles.DIRT, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
]

MAPWIDTH = len(MAP1[0])
MAPHEIGHT = len(MAP1)

#MAP ANZEIGE
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))




