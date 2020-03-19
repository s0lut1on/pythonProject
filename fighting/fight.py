import pygame
import time
import threading
import random

#init pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((1280, 720))

#title and icon
pygame.display.set_caption("Fighting")

#init game value
running = True

class BackGround:
    def __init__(self):
        self.background = pygame.image.load('bg.png')
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.x = 0
        self.x2 = self.background.get_width() - 50
        self.width = self.background.get_width()
        self.height = self.background.get_height()
        screen.blit(self.background, (self.x, 0))
        screen.blit(self.background, (self.x2, 0))

    def update(self):
        self.x -= 1.4
        self.x2 -= 1.4
        if self.x < -self.background.get_width():
            self.x = self.background.get_width()
        if self.x2 < -self.background.get_width():
            self.x2 = self.background.get_width()
            
        screen.blit(self.background, (self.x, 0))
        screen.blit(self.background, (self.x2, 0))

class Player:
    def __init__(self):
        self.x = 200
        self.y = 300
        self.count = 1
        self.image = pygame.image.load(str(self.count)+'.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += 8
        self.count += 1
        if self.count == 5:
            self.count = 1
        self.image = pygame.image.load(str(self.count)+'.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        screen.blit(self.image, (self.x, self.y))