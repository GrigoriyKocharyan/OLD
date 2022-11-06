import pygame
import random

a = int(input())
n = int(input())
m = 0
pygame.init()
win = pygame.display.set_mode((a, a))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    win.fill((255, 255, 255))
    for i in range(int(-a / n), int(a), int(a / n) * 2):
        for b in range(0, int(a), int(a / n)*2):
            pygame.draw.rect(win, (0, 0, 0), (i,b, int(a / n), int(a / n)))
    for l in range(int(-a / n), int(a), int(a / n) * 2):
        for q in range(0, int(a), int(a / n)*2):
            pygame.draw.rect(win, (0, 0, 0), (l-a/n,q+a/n, int(a / n), int(a / n)))
    pygame.display.update()
