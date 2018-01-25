import pygame as pg

pg.init()

is_moving = 0
a = 0
clock = pg.time.Clock()
b = 0

game_display = pg.display.set_mode((240, 176))

while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            b = 1
        elif event.type == pg.KEYUP:
            b = 0

    if b == 1 and is_moving == 0:
        is_moving = 1
    if is_moving == 1:
        a += 1
        print(a)
        if a == 32:
            is_moving = 0
            a = 0

    clock.tick(5)

    
