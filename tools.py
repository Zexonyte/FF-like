"""
Some functions for the RPG.
"""
import copy, sys, os
        
def array_check(array):
    for row in array:
        if len(array[0]) != len(row):
            raise ValueError("'array' is not a perfect array'")
        if type(row) != list:
            raise TypeError("row at "+str(array.index(row))+" is not type list")

def print_array(array):
    a = ""
    for s in array:
        a += (str(*s) + "\n")
    return a
        
def array_crop(
    array,
    u_crop,
    l_crop,
    d_crop,
    r_crop,
    rad,
    pad_int=0
    ):
    """crop a list."""
    #error checking
    if isinstance(array, list) != True:
        raise TypeError("'array' is not of type list")

    for l in array:
        if isinstance(l, list) != True:
            raise TypeError("A row in 'array' is not of type list")
        elif len(array[0]) != len(l):
            print(*array, sep='\n')
            raise ValueError("'array' is not a perfect array")

    if (isinstance(u_crop, int) != True or
        isinstance(l_crop, int) != True or
        isinstance(d_crop, int) != True or
        isinstance(r_crop, int) != True):
        raise TypeError("One or more crop arguments are not of the int type")

    a = copy.deepcopy(array)
    
    for _ in range(0, u_crop): #upper crop
        del a[0]
    #print_array(a)
    
    for l in range(0, len(a)): #left crop, l and r crop are slightly more complicated
        for _ in range(0, l_crop):
            del a[l][0]
    #print_array(a)

    for l in range(0, d_crop - 1): #down crop
        del a[-1]
    #print_array(a)

    for l in range(0, len(a)): #right crop
        for i in range(0, r_crop - 1):
            del a[l][-1]
    #print_array(a)

    return a

def find_data(
    filename,
    path="Images"
    ):
    if getattr(sys, "frozen", False): #frozen
        datadir = os.path.dirname(sys.executable)
        return os.path.join(datadir, filename)
    else: #unfrozen, source
        datadir = os.path.dirname(__file__)
        return os.path.join(datadir, path, filename)

def test():
    if __name__ == "__main__":
        return
    else:
        array = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 2, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
            ]

        """
        for s in array:
            print(*s)
        """
        #coordinates and radius (range in reality, renamed to avoid namespace collision)
        #are formatted as (x, y)
        #note: rad can only be in a rectangle shape, not a circle
        pos = (4, 2)
        rad = (1, 1)

        u = pos[1] - rad[1]
        l = pos[0] - rad[0]
        d = len(array) - pos[1] - rad[1] - 1
        r = len(array[0]) - pos[0] - rad[0] - 1
     
        for s in array_crop(array, u, l, d, r, (7, 5)):
            print(*s)

if __name__ == "__main__":
    test()
else:
    pass
