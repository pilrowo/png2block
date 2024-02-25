def get_face(img, face = "top"):
    PIXEL = 0.0625 # of a block
    NORTH = [32, 0]
    BOTTOM = [0, 16]
    WEST = [16, 16]
    TOP = [32, 16]
    EAST = [48, 16]
    SOUTH = [32, 32]
    SIZE = 16

    faces = {
        "north":NORTH,
        "bottom":BOTTOM,
        "west":WEST,
        "top":TOP,
        "east":EAST,
        "south":SOUTH
    }

    start_coords = faces[face]
    required_coords = []
    

    for y in range(SIZE):
        for x in range(SIZE):
            new_coord = [start_coords[0] + x, start_coords[1] + y]
            required_coords.append(new_coord)
    
    #print(img)

    for coord in required_coords:
        ##print(coord)
        y = coord[1]
        x = coord[0]
        ##print("yargh" + img[y][x])
        #face_list.append([ img[coord][1], img[coord][0] ])

    ##print(img[start_coords[1]][start_coords[0]])

    face_list = [["" for x in range(SIZE)] for y in range(SIZE)]
    for y, row in enumerate(face_list):
        for x, val in enumerate(row):
            face_list[y][x] = img[start_coords[1]+y][start_coords[0]+x]

    return face_list