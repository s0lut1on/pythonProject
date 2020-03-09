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
#int background
background = pygame.image.load('bg.png')
background = pygame.transform.scale(background, (800, 600))
backgroundX = 0
backgroundX2 = background.get_width() - 50

#init bird
countBird = 1
birdX = 200
birdY = 300

#init pipe
spacing_pipe = 80
pipe_x = 0
pipe_width = 30
pipe_up = pygame.image.load('tp.png')
pipe_down = pygame.image.load('bp.png')
pipe_up_height = random.randrange(50, 310, 10)
pipe_down_height = background.get_height() - pipe_up_height - spacing_pipe

def update_background(backgroundX, backgroundX2):
    backgroundX -= 1.4
    backgroundX2 -= 1.4
    if backgroundX < background.get_width() * -1:  # If our bg is at the -width then reset its position
        backgroundX = background.get_width()
    if backgroundX2 < background.get_width() * -1:
        backgroundX2 = background.get_width()

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        birdY -= 28

    #background create
    update_background(backgroundX, backgroundX2)
    screen.blit(background, (backgroundX, 0))
    screen.blit(background, (backgroundX2, 0))
    
    #bird create
    birdImage = pygame.image.load(str(countBird)+'.png')
    birdImage = pygame.transform.scale(birdImage, (50, 50))
    screen.blit(birdImage, (birdX, birdY))
    birdY += 8
    countBird += 1
    if (countBird == 5):
        countBird = 1
    
    #pipe create
    if (pipe_x == 0):
        pipe_x = background.get_width() - 50
        pipe_up_height = random.randrange(50, 400, 10)
        pipe_down_height = 600 - pipe_up_height - spacing_pipe
        pipe_up = pygame.transform.scale(pipe_up, (pipe_width, pipe_up_height))
        pipe_down = pygame.transform.scale(pipe_down, (pipe_width,  pipe_down_height))
    else:
        screen.blit(pipe_up, (pipe_x, 0))
        screen.blit(pipe_down, (pipe_x, 600 - pipe_down_height))
        pipe_x -= 10

    #check bird touch pipe
    if birdX >= pipe_x and birdX <= pipe_x + pipe_width:
        if (birdY <= pipe_up_height or birdY >= pipe_up_height + spacing_pipe):
            running = False

    pygame.display.update()
    time.sleep(0.01)

    
