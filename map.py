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
    TREE1 = 4
    TREE2 = 5

#Game dimensions
TILESIZE = 50

#Dictionary linking tiles
TEXTURES = {
    Tiles.DIRT: pygame.transform.scale(pygame.image.load('Level/ground.png'), (TILESIZE, TILESIZE)),
    Tiles.GRASS: pygame.transform.scale(pygame.image.load('Level/grass.png'), (TILESIZE, TILESIZE)),
    Tiles.WATER: pygame.transform.scale(pygame.image.load('Level/water.png'), (TILESIZE, TILESIZE)),
    Tiles.WALL: pygame.transform.scale(pygame.image.load('Level/wall.png'),   (TILESIZE, TILESIZE)),
    Tiles.TREE1: pygame.transform.scale(pygame.image.load('Level/trees/tree.png'),(TILESIZE, TILESIZE)),
    Tiles.TREE2: pygame.transform.scale(pygame.image.load('Level/trees/tree_1.png'),(TILESIZE, TILESIZE))
}

#Tiles to be displayed
MAP1= [
   [Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WALL, Tiles.WALL, Tiles.WALL],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WALL, Tiles.WALL, Tiles.WALL],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER],
]


MAP2= [
   [Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.TREE1, Tiles.TREE2, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.TREE1, Tiles.TREE2, Tiles.WATER],
   [Tiles.WALL, Tiles.WALL, Tiles.WALL, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WALL, Tiles.WALL, Tiles.WALL],
   [Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT],
   [Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.DIRT, Tiles.DIRT, Tiles.DIRT],
   [Tiles.WALL, Tiles.WALL, Tiles.WALL, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WALL, Tiles.WALL, Tiles.WALL],
   [Tiles.WATER, Tiles.TREE1, Tiles.TREE2, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.TREE1, Tiles.TREE2, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER],
]

MAP3= [
   [Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WALL, Tiles.WALL, Tiles.WALL, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.DIRT, Tiles.DIRT, Tiles.DIRT, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WALL, Tiles.WALL, Tiles.WALL, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.GRASS, Tiles.WATER],
   [Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER, Tiles.WATER],
]



MAP1_start = [50, 300]
MAP1_oldPosition = [18 * TILESIZE, 6 * TILESIZE]
MAP1_nextLevelRects = [
    pygame.Rect(19 * TILESIZE, 6 * TILESIZE, TILESIZE, TILESIZE),
    pygame.Rect(19 * TILESIZE, 7 * TILESIZE, TILESIZE, TILESIZE)
]
MAP1_previousLevelRect = None

MAP2_start = [50, 300]
MAP2_oldPosition = [18 * TILESIZE, 6 * TILESIZE]
MAP2_nextLevelRects = [
    pygame.Rect(19 * TILESIZE, 6 * TILESIZE, TILESIZE, TILESIZE),
    pygame.Rect(19 * TILESIZE, 7 * TILESIZE, TILESIZE, TILESIZE)
]
MAP2_previousLevelRect = [
    pygame.Rect(0 * TILESIZE, 6 * TILESIZE, TILESIZE, TILESIZE),
    pygame.Rect(0 * TILESIZE, 7 * TILESIZE, TILESIZE, TILESIZE)
]

MAP3_start = [50, 300]
MAP3_oldPosition = None
MAP3_nextLevelRects = None
MAP3_previousLevelRect = [
    pygame.Rect(0 * TILESIZE, 6 * TILESIZE, TILESIZE, TILESIZE),
    pygame.Rect(0 * TILESIZE, 7 * TILESIZE, TILESIZE, TILESIZE)
]

MAPWIDTH = len(MAP1[0])
MAPHEIGHT = len(MAP1)

#MAP ANZEIGE
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))



class Level:
    def __init__(self, map, startPosition, previousPosition, nextLevelRects, previousLevelRects):
        self.map = map
        self.startPosition = startPosition
        self.previousPosition = previousPosition
        self.nextLevelRect = nextLevelRects
        self.previousLevelRect = previousLevelRects

    def isOnChangePosition(self, spielfigur):

        if self.nextLevelRect is not None:
            for changePosition in self.nextLevelRect: #type: pygame.Rect
                if changePosition.colliderect(spielfigur.rect):
                    return 'next'
        if self.previousLevelRect is not None:
            for changePosition in self.previousLevelRect: #type: pygame.Rect
                if changePosition.colliderect(spielfigur.rect):
                    return 'previous'

        return False

l1 = Level(MAP1, MAP1_start, MAP1_oldPosition, MAP1_nextLevelRects, MAP1_previousLevelRect)
l2 = Level(MAP2, MAP2_start, MAP2_oldPosition, MAP2_nextLevelRects, MAP2_previousLevelRect)
l3 = Level(MAP3, MAP3_start, MAP3_oldPosition, MAP3_nextLevelRects, MAP3_previousLevelRect)
levelHolder = [l1, l2, l3]

class Spielkachel(pygame.Rect):
    def __init__(self, typ, x, y):
        super().__init__(x, y, TILESIZE, TILESIZE)
        self.type = typ

class Map:

    def __init__(self, map):
        self.map = [[0 for y in range(MAPWIDTH)] for x in range(MAPHEIGHT)]

        for x in range(MAPHEIGHT):
            for y in range(MAPWIDTH):
                self.map[x][y] = Spielkachel(map[x][y], y * TILESIZE, x * TILESIZE)

    def draw(self):
        for x in range(0, MAPHEIGHT):
            for y in range(0, MAPWIDTH):
                texture = self.map[x][y].type
                DISPLAYSURFACE.blit(TEXTURES[texture], (y * TILESIZE, x * TILESIZE))

    def returnRectList(self):
        rectList = [0 for x in range(MAPWIDTH * MAPHEIGHT)]

        i = 0
        for x in range(MAPHEIGHT):
            for y in range(MAPWIDTH):
                rectList[i] = self.map[x][y]
                i += 1
        return rectList
