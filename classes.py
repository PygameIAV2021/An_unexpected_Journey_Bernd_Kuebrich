import pygame
from map import *

spielfeld = [[0 for y in range(MAPWIDTH)] for x in range(MAPHEIGHT)]

class Spielfiguren:
    def __init__(self, name, pos_x, pos_y, look, speed=20):
        self.name = name
        self.speed = speed
        self.look = look
        self.rect = pygame.Rect(pos_x, pos_y, TILESIZE, TILESIZE)

    def tryToMove(self, diffx, diffy):
        # diffx = 0
        # diffy = 0
        #
        # if direction == 'top:
        #     diffx = self.speed
        # elif direction == 'left':
        #     diffy = -1* self.speed
        #todo: anstatt diffX und diffy einfach 'top', 'down', left, right übergeben
        #todo: überprüfe ob man über rand geht
        #todo: link frame machen

        collisionList = [0 for x in range(MAPWIDTH*MAPHEIGHT)]
        i = 0
        for x in range(MAPHEIGHT):
            for y in range(MAPWIDTH):
                collisionList[i] = spielfeld[x][y]
                i += 1

        self.rect.move_ip(diffx, diffy) #verändere dich um diffx und diffy

        result = self.rect.collidelistall(collisionList) #liefert index (aus collisionList) von allen rects mit kollisionen

        print("collision with: ")
        for index in result:
            print(collisionList[index].type)
            if collisionList[index].type in [Tiles.WATER, Tiles.WALL]:
                self.rect.move_ip(-1*diffx, -1*diffy)
                return

class Spielkachel(pygame.Rect):
    def __init__(self, typ, x, y):
        super().__init__(x, y, TILESIZE, TILESIZE)
        self.type = typ

#Bodenkachelerkennung
for x in range(MAPHEIGHT):
    for y in range(MAPWIDTH):
        spielfeld[x][y] = Spielkachel(MAP1[x][y], y*TILESIZE, x*TILESIZE)