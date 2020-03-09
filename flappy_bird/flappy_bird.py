import pygame
import time
import threading
import random

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

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
background = pygame.image.load('bg.png')
spacing_pipe = 50
pipe_up = pygame.image.load('tp.png')
pipe_down = pygame.image.load('bp.png')
backgroundX = 0
backgroundX2 = background.get_width() - 40

#flying bird and background running
def moving_init():
    backgroundX = 0
    backgroundX2 = background.get_width() - 40

    while running:
        for i in range(1, 5):
            #init background move
            backgroundX -= 1.4
            backgroundX2 -= 1.4
            if backgroundX < background.get_width() * -1:  # If our bg is at the -width then reset its position
                backgroundX = background.get_width()
            if backgroundX2 < background.get_width() * -1:
                backgroundX2 = background.get_width()
            screen.blit(background, (backgroundX, 0))
            screen.blit(background, (backgroundX2, 0))
            #init bird fly
            birdImg = pygame.image.load(str(i) + '.png')
            birdImg = pygame.transform.scale(birdImg, (50, 50))
            screen.blit(birdImg, (200, 300))
            # pygame.display.update()
            # time.sleep(0.005)

def pipe_create():
    position_x = background.get_width() - 50
    
    pipe_up_height = random.randrange(50, 310, 10)
    pipe_down_height = background.get_height() - pipe_up_height - spacing_pipe

    pipe_up = pygame.transform.scale(pipe_up, (50, pipe_up_height))
    pipe_down = pygame.transform.scale(pipe_down, (50,  pipe_down_height))

    while position_x >= 0:
        screen.blit(pipe_up, (position_x, 0))
        screen.blit(pipe_down, (position_x, pipe_up_height + spacing_pipe))
        position_x -= 5
        # pygame.display.update()
        # time.sleep(0.005)

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False