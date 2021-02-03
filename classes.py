import pygame
from map import Map, TILESIZE, MAPHEIGHT, MAPWIDTH, DISPLAYSURFACE, Tiles
from enemies import Beast, Ganon

class Player():
    def __init__(self, name, pos, look, map: Map, speed=9, spritecounter=0, health=100, inventory = [], spritecounter_wolf_top_down = 0, spritecounter_wolf_left_right = 0):
        self.name = name
        self.map = map
        self.speed = speed
        self.look = look
        self.rect = pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE)
        self.spritecounter = spritecounter
        self.spritecounter_wolf_top_down = spritecounter_wolf_top_down
        self.spritecounter_wolf_left_right = spritecounter_wolf_left_right
        self.link_go_up = [pygame.image.load("sprites/link/link_b0.png"), pygame.image.load("sprites/link/link_b1.png"), pygame.image.load("sprites/link/link_b2.png"), pygame.image.load("sprites/link/link_b3.png"), pygame.image.load("sprites/link/link_b4.png"), pygame.image.load("sprites/link/link_b5.png"), pygame.image.load("sprites/link/link_b6.png"), pygame.image.load("sprites/link/link_b7.png")]
        self.link_go_down = [pygame.image.load("sprites/link/link_f0.png"), pygame.image.load("sprites/link/link_f1.png"), pygame.image.load("sprites/link/link_f2.png"), pygame.image.load("sprites/link/link_f3.png"), pygame.image.load("sprites/link/link_f4.png"), pygame.image.load("sprites/link/link_f5.png"), pygame.image.load("sprites/link/link_f6.png"), pygame.image.load("sprites/link/link_f4.png")]
        self.link_go_left = [pygame.image.load("sprites/link/link_l3.png"), pygame.image.load("sprites/link/link_l2.png"), pygame.image.load("sprites/link/link_l1.png"), pygame.image.load("sprites/link/link_l0.png"),  pygame.image.load("sprites/link/link_l3.png"), pygame.image.load("sprites/link/link_l4.png"), pygame.image.load("sprites/link/link_l5.png"), pygame.image.load("sprites/link/link_l6.png"), pygame.transform.scale(pygame.image.load("sprites/link.png"), (60,60,))]
        self.link_go_right = [pygame.image.load("sprites/link/link_r0.png"), pygame.image.load("sprites/link/link_r1.png"), pygame.image.load("sprites/link/link_r2.png"), pygame.image.load("sprites/link/link_r3.png"), pygame.image.load("sprites/link/link_r4.png"), pygame.image.load("sprites/link/link_r5.png"), pygame.image.load("sprites/link/link_r6.png"), pygame.image.load("sprites/link/link_r7.png"), pygame.transform.flip(pygame.transform.scale(pygame.image.load("sprites/link.png"), (60,60)), True, False)]
        self.health = health
        self.inventory = inventory
        self.wolf_go_up = [pygame.image.load("sprites/wolf/wolf_b0.png"), pygame.image.load("sprites/wolf/wolf_b1.png"), pygame.image.load("sprites/wolf/wolf_b2.png"), pygame.image.load("sprites/wolf/wolf_b3.png"), pygame.image.load("sprites/wolf/wolf_b4.png"), pygame.image.load("sprites/wolf/wolf_b5.png"), pygame.image.load("sprites/wolf/wolf_b6.png")]
        self.wolf_go_down = [pygame.image.load("sprites/wolf/wolf_f0.png"), pygame.image.load("sprites/wolf/wolf_f1.png"), pygame.image.load("sprites/wolf/wolf_f2.png"), pygame.image.load("sprites/wolf/wolf_f3.png"), pygame.image.load("sprites/wolf/wolf_f4.png"), pygame.image.load("sprites/wolf/wolf_f5.png"), pygame.image.load("sprites/wolf/wolf_f6.png")]
        self.wolf_go_left = [pygame.image.load("sprites/wolf/wolf_l0.png"), pygame.image.load("sprites/wolf/wolf_l1.png"), pygame.image.load("sprites/wolf/wolf_l2.png"), pygame.image.load("sprites/wolf/wolf_l3.png")]
        self.wolf_go_right = [pygame.image.load("sprites/wolf/wolf_r0.png"), pygame.image.load("sprites/wolf/wolf_r1.png"), pygame.image.load("sprites/wolf/wolf_r2.png"), pygame.image.load("sprites/wolf/wolf_r3.png")]
        self.transform = False
        self.link_fight = pygame.image.load("sprites/link.png")


    def tryToMove(self, direction, current_level, beast: Beast, ganon: Ganon):

        moveX, moveY = (0, 0)

        if direction == "down":
            self.look = "down"
            if self.rect.bottom < (MAPHEIGHT * TILESIZE):  # if Bedingung damit die figur nicht über den unteren rand hinausgeht
                moveX, moveY = (0, self.speed)
        elif direction == "up":
            self.look = "up"
            if self.rect.top >= self.speed: #if Bedingung damit die Figur nicht über den oberen rand hinausgeht
                moveX, moveY = (0, -1*self.speed)
        elif direction == "right":
            self.look = "right"
            if self.rect.right < (MAPWIDTH * TILESIZE):  # if Bedingung damit die figur nicht über den rechten rand hinausgeht
                moveX, moveY = (self.speed, 0)
        elif direction == "left":
            self.look = "left"
            if self.rect.left > 0:  #if Bedingung damit die figur nicht über den linken rand hinausgeht
                moveX, moveY = (-1*self.speed, 0)

        #Spielerfigur verändert die Position
        self.rect.move_ip(moveX, moveY)

        #Rechteckliste speichern
        rectList = self.map.returnRectList()

        #liefert index (aus collisionList) von allen rects mit kollisionen
        result = self.rect.collidelistall(rectList)

        if beast.level == current_level and self.rect.colliderect(beast.rect):
            self.rect.move_ip(-1 * moveX, -1 * moveY)

        if ganon.level == current_level and self.rect.colliderect(ganon.rect):
            self.rect.move_ip(-1 * moveX, -1 * moveY)

        for index in result:
            if rectList[index].type in [Tiles.WATER, Tiles.WALL, Tiles.TREE1, Tiles.TREE2]:
                self.rect.move_ip(-1*moveX, -1*moveY)
                return

        if self.transform is False:
            self.spritecounter += 1
            if self.spritecounter > 7:
                self.spritecounter = 0
        else:
            self.spritecounter_wolf_top_down += 1
            self.spritecounter_wolf_left_right += 1
            if self.spritecounter_wolf_top_down > 6:
                self.spritecounter_wolf_top_down = 0
            if self.spritecounter_wolf_left_right > 3:
                self.spritecounter_wolf_left_right = 0

    #Spielfigur zeichnen
    def draw(self):
        if self.look == "up":
            if self.transform:
                DISPLAYSURFACE.blit(self.wolf_go_up[self.spritecounter_wolf_top_down], (self.rect.left, self.rect.top))
            else:
                DISPLAYSURFACE.blit(self.link_go_up[self.spritecounter], (self.rect.left, self.rect.top))

        elif self.look == "down":
            if self.transform:
                DISPLAYSURFACE.blit(self.wolf_go_down[self.spritecounter_wolf_top_down], (self.rect.left, self.rect.top))
            else:
                DISPLAYSURFACE.blit(self.link_go_down[self.spritecounter], (self.rect.left, self.rect.top))

        elif self.look == "left":
            if self.transform:
                DISPLAYSURFACE.blit(self.wolf_go_left[self.spritecounter_wolf_left_right], (self.rect.left, self.rect.top))
            else:
                DISPLAYSURFACE.blit(self.link_go_left[self.spritecounter], (self.rect.left, self.rect.top))

        elif self.look == "right":
            if self.transform:
                DISPLAYSURFACE.blit(self.wolf_go_right[self.spritecounter_wolf_left_right], (self.rect.left, self.rect.top))
            else:
                DISPLAYSURFACE.blit(self.link_go_right[self.spritecounter], (self.rect.left, self.rect.top))

    def changeLevel(self, position, map):
        self.rect.left = position[0]
        self.rect.top = position[1]
        self.map = map

class Sword():
    def __init__(self):
        self.name = 'Sword'
        self.image = pygame.image.load('sprites/sword.png')
        self.pos = [500, 500]
        self.placed = True
        self.inventory_pos = [400, 0]
        self.picked_up = False

class Shield():
    def __init__(self):
        self.name= 'SHIELD'
        self.image = pygame.image.load('sprites/shield.png')
        self.pos = [250, 250]
        self.placed = True
        self.inventory_pos = [300, 0]
        self.picked_up = False

class Bow():
    def __init__(self):
        self.name = 'BOW'
        self.image = pygame.transform.scale(pygame.image.load('sprites/bow.png'), (TILESIZE, TILESIZE))
        self.pos = [400, 400]
        self.placed = True
        self.inventory_pos = [350,0]
        self.picked_up = False



