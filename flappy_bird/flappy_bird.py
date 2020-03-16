import pygame
import time
import threading
import random

#init pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#init game value
running = True

class Bird:
    # x = 200
    # y = 300
    # count = 1
    def __init__(self):
        self.x = 200
        self.y = 300
        self.count = 1
        self.birdImage = pygame.image.load(str(self.count)+'.png')
        self.birdImage = pygame.transform.scale(self.birdImage, (50, 50))
        screen.blit(self.birdImage, (self.x, self.y))
        

    def update(self):
        self.y += 8
        self.count += 1
        if self.count == 5:
            self.count = 1
        self.birdImage = pygame.image.load(str(self.count)+'.png')
        self.birdImage = pygame.transform.scale(self.birdImage, (50, 50))
        screen.blit(self.birdImage, (self.x, self.y))

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
        if self.x < self.background.get_width() * -1:  # If our bg is at the -width then reset its position
            self.x = self.background.get_width()
        if self.x2 < self.background.get_width() * -1:
            self.x2 = self.background.get_width()
            
        screen.blit(self.background, (self.x, 0))
        screen.blit(self.background, (self.x2, 0))

class Pipe:
    def __init__(self, backgroundWidth, backgroundHeight):
        self.backgroundHeight = backgroundHeight
        self.backgroundWidth = backgroundWidth
        self.spacing = 80
        self.x = 0
        self.width = 30
        self.imgUp = pygame.image.load('tp.png')
        self.imgDown = pygame.image.load('bp.png')
        self.upHeight = random.randrange(50, 310, 10)
        self.downHeight = self.backgroundHeight - self.upHeight - self.spacing

    def update(self):
        if (self.x == 0):
            self.x = self.backgroundWidth - 50
            self.upHeight = random.randrange(50, 400, 10)
            self.downHeight = self.backgroundHeight - self.upHeight - self.spacing
            self.imgUp = pygame.transform.scale(self.imgUp, (self.width, self.upHeight))
            self.imgDown = pygame.transform.scale(self.imgDown, (self.width,  self.downHeight))
        else:
            screen.blit(self.imgUp, (self.x, 0))
            screen.blit(self.imgDown, (self.x, self.backgroundHeight - self.downHeight))
            self.x -= 10

#game loop
background = BackGround()
bird = Bird()
pipe = Pipe(background.width, background.height)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.y -= 28

    background.update()
    bird.update()
    pipe.update()

    #check bird touch pipe
    if bird.x >= pipe.x and bird.x <= pipe.x + pipe.width:
        if (bird.y <= pipe.upHeight or bird.y >= pipe.upHeight + pipe.spacing):
            running = False

    pygame.display.update()
    time.sleep(0.01)

    
