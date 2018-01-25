"""
The NPC class.

They will never attack, and will usually have an event.
Some may have random movement, and others may not.
This is specified with the 'can_move' kwarg.
"""

import sys, os
try:
    import pygame as pg
    import Entity as Ent
except ModuleNotFoundError as err:
    raise ModuleNotFoundError("Could not find the %s module" % err)
    
pg.init()

class NPC(Ent.Entity):
    def __init__(
        self,
        name,
        c_map,
        start,
        textures=["dummy.png"]
        ):
        """init..."""
        ###### base class init...
        Ent.Entity(
            self,
            0,
            name,
            [16, 16]
            start,
            1,
            0,
            textures,
            resize=2
            )
        
            
