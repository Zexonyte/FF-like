"""
Class for all entities, including the player.

The class is in reality split in two parts: the entity data
i.e. gold, inventory, etc. and the visuals i.e. the sprite.

Visuals:
Upon initiation, the visuals are done first, as of pre-alpha 0.0.1.
Data:
Upon initiation, the player data is done second as of pre-alpha 0.0.1.
"""
import sys, os
try:
    import pygame as pg
    import Map
    import tools as t
    import colors as col
except ModuleNotFoundError as err:
    raise ModuleNotFoundError("Couldn't find the %s module")


class Entity(pg.sprite.Sprite):
    def __init__(
        self,
        m_h,
        n,
        size,
        start,
        c_map,
        on_map,
        in_battle,
        can_move,
        textures,
        **kwargs
        ):
        """init for class..."""     
        ###### base class...
        super(Entity, self).__init__()
        ######

        ###### data...
        self.RESIZE = kwargs.get('resize', 1)
        if on_map == 1:
            self.overworld = pg.transform.scale(
                pg.image.load(t.find_data(textures[0])).convert_alpha(),
                (self.RESIZE * size[0], self.RESIZE * size[1])
                )
            
    def handle_movement(
        self,
        warpset,
        maps,
        surface,
        clock
        ):
        """"movement handler.""""
        part_dx, part_dy = 0, 0
        #walk sequence, halfway mark...
        if self.movement == 0:
            return
        else:
            if (self.coords[0] + self.dx > len(self.c_map.MAP['COLL_BASE'][self.coords[1]]) - 2 or
                self.coords[0] + self.dx < 0 or
                self.c_map.MAP['COLL_BASE'][self..coords[1]][self.coords[0] + self.dx] == 1):
                pass
            else:
                if self.dx < 0:
                    part_dx = -1
                elif self.dx > 0:
                    part_dx = 1

            if (self.coords[1] + self.dy > len(self.c_map.MAP['COLL_BASE']) - 2 or
                self.coords[1] + self.dy < 0 or
                self.c_map.MAP['COLL_BASE'][self.coords[1] + self.dy][self.coords[0]] == 1):
                pass
            else:
                if self.dy < 0:
                    part_dy = -1
                elif self.dy > 0:
                    part_dy = 1

            #actual new placement and coords affection...
            if (self.coords[0] + self.dx in range(0, len(self.c_map.MAP['TILE_BASE'][self.coords[1]])) and
                self.c_map.MAP['COLL_BASE'][self.coords[1]][self.coords[0] + self.dx] != 1):
                self.coords[0] += self.dx
            if (self.coords[1] + self.dy in range(0, len(self.c_map.MAP['TILE_BASE'])) and
                self.c_map.MAP['COLL_BASE'][self.coords[1] + self.dy][self.coords[0]] != 1):
                self.coords[1] += self.dy

            surface.fill(col.BLACK)

            #checking if player walked into warp tile...
            if self.c_map.MAP['WARP_BASE'][self.coords[1]][self.coords[0]] in warp_set:
                old_coords = copy.copy(self.coords)
                self.coords = copy.copy(warp_set[
                    self.c_map.MAP['WARP_BASE'][self.coords[1]][self.coords[0]]
                    ][1])
                self.c_map = maps[
                        warp_set[
                            player.c_map.MAP['WARP_BASE'][old_coords[1]][old_coords[0]]
                            ][0]
                        ]
                surface.fill(col.BLACK)
                self.c_map.load_map(game_display, player.coords, render_dist)
                player.dx, player.dy = 0, 0
                del old_coords
            
            
        
        
        
