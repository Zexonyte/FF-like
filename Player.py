"""
The player class.

The player controls this class. It is also the only class
to have the 'handle-keys' function.
"""

try:
    import pygame as pg
    
    import Map
    #import Entity as Ent
    import colors as col
    import tools as t
except ModuleNotFoundError as err:
    raise ModuleNotFoundError("Could not find the %s module" % err)

pg.init()
    
class Player:
    def __init__(
        self,
        name,
        sizes,
        c_map,
        start,
        textures=["dummy.png"],
        **kwargs
        ):
        """Init for player class."""
        self.SIZE = (
                        kwargs.get('resize', 1) * sizes[0][0],
                        kwargs.get('resize', 1) * sizes[0][1]
                        )
        #super(Player, self).__init__()
        self.TEXTURE = pg.transform.scale(
            pg.image.load(t.find_data(textures[0])),
            self.SIZE
            )
        self.coords = start
        self.c_map = c_map
        self.dx, self.dy = 0, 0
        self.is_moving = 0
        self.t = 0
        self.a = 0
        
    def draw(
        self,
        surface
        ):
        """draw onto current map."""
        surface.blit(
            self.TEXTURE,
            (
                (0.5 * surface.get_size()[0]) - (0.5 * self.SIZE[0]),
                (0.5 * surface.get_size()[1]) - (0.5 * self.SIZE[1]) - 4
                )
            )
            
    def handle_keys(
        self,
        event
        ):
        """handle an event if it's a key press/depress."""
        if event.type == pg.KEYDOWN:
            if self.is_moving == 0:
                if (event.key == pg.K_LEFT and
                    self.coords[0] - 2 >= 0 and
                    self.c_map.MAP['COLL_BASE'][self.coords[1]][self.coords[0] - 2] != 1):
                    self.dx = -2
                elif (event.key == pg.K_RIGHT and
                      self.coords[0] + 2 < len(self.c_map.MAP['TILE_BASE'][self.coords[1]]) - 1 and
                      self.c_map.MAP['COLL_BASE'][self.coords[1]][self.coords[0] + 2] != 1):
                    self.dx = 2
                elif (event.key == pg.K_UP and
                      self.coords[1] - 2 > 0 and
                      self.c_map.MAP['COLL_BASE'][self.coords[1] - 2][self.coords[0]] != 1):
                    self.dy = -2
                elif (event.key == pg.K_DOWN and
                      self.coords[1] + 2 < len(self.c_map.MAP['TILE_BASE']) - 1 and
                      self.c_map.MAP['COLL_BASE'][self.coords[1] + 2][self.coords[0]] != 1):
                    self.dy = 2
                    print(self.dy)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                self.dx = 0
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                self.dy = 0
