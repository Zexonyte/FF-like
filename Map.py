"""

Map class for my RPG.
This comes with a custom-written tileloader.
"""
import os, sys
try:
    import pygame as pg
    import tools as t
except ModuleNotFoundError as err:
    raise ModuleNotFoundError("Could not find the %s module" % err)

pg.init()
    
class Map:
    def __init__(
        self,
        t_map,
        c_map,
        w_map,
        t_size,
        tileset,
        **kwargs
        ):
        """Initiate the map"""
        ###### error checking...
                
        if (type(t_map) != list or
            type(c_map) != list or
            type(w_map) != list):
            raise TypeError("One or more arrays are not type list")

        t.array_check(t_map)
        t.array_check(c_map)
        t.array_check(w_map)

        if (type(t_size[0]) != int or
            type(t_size[1]) != int):
            raise TypeError("One or more values in 't_size' are not type int")
              
        if type(t_size) != tuple:
            raise TypeError("'t_size' is not type tuple")

        if len(t_size) != 2:
            raise ValueError("'t_size' is not a length of 2")
        ######

        ###### resizing and tileset
        self.RESIZE = kwargs.get('resize', 1)
        self.TILESET = pg.image.load(t.find_data(tileset)).convert_alpha()
        self.WIDTH, self.HEIGHT = self.TILESET.get_size()
        if (self.WIDTH % t_size[0] != 0 or
            self.HEIGHT % t_size[1] != 0):
            raise ValueError("'tileset' and 't_size' do not fit")

        if self.RESIZE > 1:
            self.TILESET = pg.transform.scale(
                self.TILESET, (self.WIDTH * self.RESIZE, self.HEIGHT * self.RESIZE)
                )
            self.WIDTH, self.HEIGHT = self.TILESET.get_size()
            #if the above happened remeasure the size just in case
        self.T_SIZE = (t_size[0] * self.RESIZE, t_size[1] * self.RESIZE)
        ######

        ###### map...
        self.MAP = {
            'TILE_BASE' : t_map,
            'COLL_BASE' : c_map,
            'WARP_BASE' : w_map
            }

        ###### tiles
        self.TILES = {}

        self.MIN_ID = 0
        self.MAX_ID = 0

        a = 0

        for row in range(0, int(self.WIDTH / self.T_SIZE[0])):
            for column in range(0, int(self.HEIGHT / self.T_SIZE[1])):
                rect = (
                    row * self.T_SIZE[1],
                    column * self.T_SIZE[0],
                    self.T_SIZE[0],
                    self.T_SIZE[1]
                    )
                self.TILES[str(a)] = self.TILESET.subsurface(rect)
                a += 1

        self.MAX_ID = a - 1#setting max_id is for error checking later
        ######

    def load_map(
        self,
        surface,
        player_pos,
        render_dist,
        push=None
        ):
        """built in tileloader."""
        ###### error-checking...
        if (type(player_pos) != list or
            type(render_dist) != list):
            raise TypeError("'One or more arguments are not type list")

        for i in player_pos:
            if type(i) != int:
                raise TypeError("One or more values in 'player_pos' are not type int")

        for i in render_dist:
            if type(i) != int:
                raise TypeError("One or more values in 'render_dist' are not type int")

        if len(player_pos) != 2 or len(render_dist) != 2:
            raise ValueError("One or more arguments are not length 2")

        if type(surface) != pg.Surface:
            raise TypeError("argument 'surface' is not type pg.Surface")
        ######

        ###### crop (for optimization)
        #arguments are in form of [x, y]
        u = player_pos[1] - render_dist[1] 
        l = player_pos[0] - render_dist[0]
        d = len(self.MAP['TILE_BASE']) - (player_pos[1] + render_dist[1] + 1)
        r = len(self.MAP['TILE_BASE'][0]) - (player_pos[0] + render_dist[0] + 1)
        
        a = t.array_crop(
            self.MAP['TILE_BASE'],
            u,
            l,
            d,
            r,
            [
                (surface.get_size()[0] // self.T_SIZE[0]) // 2,
                (surface.get_size()[1] // self.T_SIZE[1]) // 2
             ]
            )
        #padding
        u_pad = 0
        l_pad = 0

        if u < 0:
            u_pad = abs(u)
        if l < 0:
            l_pad = abs(l)
        ######

        ###### push...
        x_push, y_push = 0, 0
        if push != None:
            if push[0] == "x":
                x_push = push[1]
            elif push[0] == "y":
                y_push = push[1]
            else:
                pass
            #print(x_push, y_push)
        ######

        ###### main tileloader...
        for x in range(0, len(a)):
            for y in range(0, len(a[x])):
                if (a[x][y] > self.MAX_ID or
                    a[x][y] < self.MIN_ID):
                        continue
                else:
                    surface.blit(
                        self.TILES[str(a[x][y])],
                        (
                            (y + l_pad) * self.T_SIZE[1] - x_push,
                            (x + u_pad) * self.T_SIZE[0] - y_push
                            )
                        )
        ######
                    
        ###### free up memory.
        del a
        del u_pad, l_pad
        del u, l, d, r
        del x_push, y_push
        ######
