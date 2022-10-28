import pygame
from pygame.draw import rect, polygon, circle

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))
screen.fill('purple')

circle(screen, (255, 255, 0), (400, 300), 200)
circle(screen, (0, 0, 0), (400, 300), 200, 10)
rect(screen, (0, 0, 0), (300, 400, 200, 40), 0, 20, 20, 20, 20)
circle(screen, 'red', (290, 230), 40)
circle(screen, 'red', (510, 230), 30)
circle(screen, 'black', (290, 230), 40, 5)
circle(screen, 'black', (510, 230), 30, 5)

circle(screen, 'black', (320, 230), 10)
circle(screen, 'black', (490, 230), 10)

polygon(screen, 'black', [(250, 175), (260, 150), (350, 210)])
polygon(screen, 'black', [(550, 190), (540, 165), (450, 225)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
