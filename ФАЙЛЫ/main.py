import pygame as pg
import sys


t = 10

WHITE = (255, 255, 255)
BLUE = (0, 255, 0)
 
sc = pg.display.set_mode((400, 300))
sc.fill(WHITE)
pg.display.update()
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
 
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    
    
    if pressed[0]:
        
        pos = pg.mouse.get_pos()
        while pressed[0]:
            pressed = pg.mouse.get_pressed()
            sc.fill(WHITE)
            pos1=pg.mouse.get_pos()
            pg.draw.line(sc, BLUE, (pos), (pos1[0], pos[1]), t)
            pg.draw.line(sc, BLUE, (pos1[0], pos[1]), (pos1[0], pos1[1]), t)
            pg.draw.line(sc, BLUE, (pos1[0], pos1[1]), (pos[0], pos1[1]), t)
            pg.draw.line(sc, BLUE, (pos[0], pos1[1]), (pos), t)
            print(pos1)
            pg.display.update()
            
        pg.display.update()
    else:
        sc.fill(WHITE)
        pg.display.update()
        
        
