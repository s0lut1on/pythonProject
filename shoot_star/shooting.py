import pygame
import time
import threading
import random

#init pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((500, 800))

#title and icon
pygame.display.set_caption("Shooting star")

#init game value
running = True

class BackGround:
    def __init__(self):
        self.background = pygame.image.load('background.jpg')
        self.background = pygame.transform.scale(self.background, (500, 800))
        self.y = 0
        self.y2 = self.background.get_height()
        screen.blit(self.background, (0, self.y))
        screen.blit(self.background, (0, self.y2))

    def update(self):
        self.y += 8
        self.y2 += 8
        if self.y > self.background.get_height():
            self.y = -self.background.get_height()
        if self.y2 > self.background.get_height():
            self.y2 = -self.background.get_height()
        screen.blit(self.background, (0, self.y))
        screen.blit(self.background, (0, self.y2))
        
class Ship:
    def __init__(self):
        self.image = pygame.image.load('ship.png')
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.x = 250
        self.y = 600

    def update(self):
        screen.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.x =  x
        self.y = y

    def update(self):
        self.y -= 16

class StaticEnemy:
    def __init__(self):
        self.image = pygame.image.load('staticEnemy.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.x =  random.randrange(0, 500, 10)
        self.y = 0

    def update(self):
        self.y += 16

background = BackGround()
ship = Ship()
listBullet = []
listStaticEnemy = []
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        listBullet.append(Bullet(ship.x + 25, ship.y - 30))
    if keys[pygame.K_UP]:
        ship.y -= 10
    if keys[pygame.K_DOWN]:
        ship.y += 10
    if keys[pygame.K_RIGHT]:
        ship.x += 10
    if keys[pygame.K_LEFT]:
        ship.x -= 10

    #check shoot star
    for i in range(len(listBullet)-1, -1, -1):
        for j in range(len(listStaticEnemy)-1, -1, -1):
            if (listStaticEnemy[j].x > listBullet[i].x and listStaticEnemy[j].x < (listBullet[i].x + 30)
                and (listStaticEnemy[j].y + 30) > listBullet[i].y and listStaticEnemy[j].y < listBullet[i].y):
                listStaticEnemy.pop(j)
    
    #draw item
    background.update()
    ship.update()
    if random.randrange(0, 2, 1) % 2 != 0: 
        listStaticEnemy.append(StaticEnemy())
    for enemy in listStaticEnemy:
        if enemy.y <= 800:
            enemy.update()
            screen.blit(enemy.image, (enemy.x, enemy.y))
        else:
            listStaticEnemy.pop(0)
    for bullet in listBullet:
        if bullet.y >= 0:
            bullet.update()
            screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            listBullet.pop(0)

    pygame.display.update()
    time.sleep(0.05)