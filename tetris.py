import pygame
import gameLogic


pygame.init()

crashed = False

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Tetris')


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
