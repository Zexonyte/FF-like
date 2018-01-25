"""
RPG using pygame. The gameplay is going to be like that of
the pre-Playstation era of Final Fantasy games.
"""
version = "0.0.5"
#current goal: npcs
import copy, sys
try:
    import pygame as pg

    import colors as col
    import Map

    import Player as play
except ModuleNotFoundError as err:
    raise ModuleNotFoundError("Could not find the %s module" % err)

pg.init()

#split stuff up into 8x8 chunks. (later)

###### display setup
resize=2
DISPLAY_WIDTH = 240 * resize
DISPLAY_HEIGHT = 176 * resize

game_display = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("RPG pre-alpha "+str(version))

game_display.fill(col.BLACK) #initial fill...
pg.display.update()
######

###### non-display var setup...
clock = pg.time.Clock()
closed = False
######

###### maps...
x = 10
y = 10
map1 = {
    'tileset' : "SmallForestTile.png",
    'tile_base' : [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 59, 59, 6, 6, 6, 6, 0, 0, 59, 59, 0, 0],
        [0, 0, 59, 59, 6, 6, 6, 6, 0, 0, 59, 59, 0, 0],
        [0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 58, 58, 0, 0],
        [0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 58, 58, 0, 0],
        [0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 59, 59, 0, 0],
        [0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 59, 59, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
    'collision_base' : [ ## [0 for _ in range(0, y)] for _ in range(0, x)
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ],
    'warp_base' : [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 'a', 0, 0, 0, 0, 0, 0, 0, 'b', 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'c', 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    }

map2 = {
  'tileset' : "SmallOverworldTile.png",
  'tile_base' : [
        [21, 21, 21, 21, 21, 21],
        [21, 16, 15, 15, 20, 21],
        [21, 11, 10, 10, 14, 21],
        [21, 11, 10, 10, 14, 21],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ],
  'collision_base' : [
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 0, 0, 1, 1],
      [1, 1, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]
      ],
  'warp_base' : [
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 'd', 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]
      ]
  }

inside = Map.Map(
    map1['tile_base'],
    map1['collision_base'],
    map1['warp_base'],
    (8, 8),
    map1['tileset'],
    resize=resize
    )

outside = Map.Map(
    map2['tile_base'],
    map2['collision_base'],
    map2['warp_base'],
    (8, 8),
    map2['tileset'],
    resize=resize
    )

maps = {
    "inside" : inside,
    "outside" : outside
    }

warp_set = {
    "a" : ["inside", [10, 4]],
    "b" : ["inside", [2, 4]],
    "c" : ["outside", [2, 4]],
    "d" : ["inside", [10, 4]]
    }
######

###### player...
player = play.Player(
    "Nessh",
    [(16, 16)],
    outside,
    [4, 4],
    textures=["dummy.png"],
    resize=resize
    )

######

def Quit():
    pg.quit()
    sys.exit()

###### mainloop...
def main():
    render_dist = [14, 10]
    part_dx, part_dy = player.dx, player.dy
    p = ["", 0]
    fps = 30
    
    game_display.fill(col.BLACK)
    player.c_map.load_map(
        game_display,
        player.coords,
        render_dist
        )
    while True:
        old_coords = copy.copy(player.coords)
        
        for event in pg.event.get(): #event handler...

            if event.type == pg.QUIT:
                Quit()
            elif player.is_moving == 0 and event.type == pg.KEYDOWN:
                player.a = 1
                player.handle_keys(event)
            elif event.type == pg.KEYUP:
                player.a = 0

        #walk sequence...
        if (player.a == 1 and
            player.is_moving == 0 and
            player.coords[0] + player.dx in range(0, len(player.c_map.MAP['TILE_BASE'])) and
            player.coords[1] + player.dy in range(0, len(player.c_map.MAP['TILE_BASE'][player.coords[1]]))):
            player.is_moving = 1
        if player.is_moving == 1:
            if player.dx < 0 or player.dy < 0:
                player.t -= 1
            if player.dx > 0 or player.dy > 0:
                player.t += 1
            print(player.t)
            if abs(player.t) > 16:
                player.t = 0
                player.is_moving = 0

                #actual new placement and coords affection...
                player.coords[0] += player.dx
                player.coords[1] += player.dy


                #checking if player walked into warp tile...
                if player.c_map.MAP['WARP_BASE'][player.coords[1]][player.coords[0]] in warp_set:
                    player.coords = copy.copy(warp_set[
                        player.c_map.MAP['WARP_BASE'][player.coords[1]][player.coords[0]]
                        ][1])
                    player.c_map = maps[
                            warp_set[
                                player.c_map.MAP['WARP_BASE'][old_coords[1]][old_coords[0]]
                                ][0]
                            ]
                
                    player.dx, player.dy = 0, 0
                    del old_coords
                    
            else:
                if player.dx != 0:
                    p = ["x", 2 * player.t]
                if player.dy != 0:
                    p = ["y", 2 * player.t]
                game_display.fill(col.BLACK)
                player.c_map.load_map(
                    game_display,
                    player.coords,
                    render_dist,
                    push=p
                    )

        #print(clock.get_time())
        player.draw(game_display)
        pg.display.update()
        clock.tick(fps)
######
        
if __name__ == "__main__": main()
