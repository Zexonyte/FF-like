import pickle
import Map

map1 = {
    'tile_base' : [[42 for _ in range(0, 25)] for _ in range(0, 25)],
    'collision_base' : [[0 for _ in range(0, 25)] for _ in range(0, 25)],
    'warp_base' : [[0 for _ in range(0, 25)] for _ in range(0, 25)]
    }

forest = Map.Map(
    

with open("forest.pickle", "wb") as f:
    pickle.dump(map1, f)
