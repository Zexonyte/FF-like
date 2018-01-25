import os

try:
    import Map
    import colors as col
    import pygame as pg

except ModuleNotFoundError as err:
    raise ModuleNotFoundError("Couldn't find %s" % err)

pg.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

game_display = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("test")

game_display.fill(col.BLACK)

t = [
    [38,

forest = Map.Map(
    ,
    ,
    ,
    "ForestTile.png",
    (16, 16),
    game_display,
    resize=2
    )

closed = False
clock = pg.time.Clock()

while not closed:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            closed = True

    game_display.fill(col.BLACK)
    forest.load_map()
    pg.display.update()
    clock.tick(60)

pg.quit()
quit()
