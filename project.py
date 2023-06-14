import pygame
import sys

pygame.font.init()

sc = pygame.display.set_mode((300, 200))
sc.fill((255, 255, 255))

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Hello Привет', True,
                  (180, 0, 0))



sc.blit(text1, (10, 50))

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()