from copy import copy

def generate_function(block_dict, tag, colour_dict):
    SIZE = 16
    PIXEL = 0.0625 # of a block
    TINY = 0.0001
    function_list = []

    for direction in ["north", "south", "east", "west"]:

        # NORTH FACE
        #block_dict["north"]
        id_dict = copy(block_dict[direction])

        #print(id_dict)

        for y, row in enumerate(id_dict):
            for x, val in enumerate(row):
                ##rint(val)
                id_dict[y][x] = colour_dict[val]

        ##print(id_dict)

        coord_x = 0
        coord_y = 0

        for y, row in enumerate(id_dict):
            for x, val in enumerate(row):

                if direction == "north":
                    command = 'summon block_display ~'+ str(coord_x - PIXEL) +' ~'+ str(coord_y - PIXEL) +' ~'+ str(-TINY) +' {Tags:["'+ tag +'"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.0625f,0.0625f,0f]},block_state:{Name:"minecraft:'+ id_dict[y][x] +'"}}'
                
                elif direction == "south":
                    coord = str((coord_x - 1))
                    command = 'summon block_display ~'+ coord +' ~'+ str(coord_y - PIXEL) +' ~'+ str(TINY + 1) +' {Tags:["'+ tag +'"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.0625f,0.0625f,0f]},block_state:{Name:"minecraft:'+ id_dict[y][x] +'"}}'

                elif direction == "east":
                    coord = str(coord_x + 1 - PIXEL)
                    command = 'summon block_display ~'+ str((TINY)) +' ~'+ str(coord_y - PIXEL) +' ~'+ coord +' {Tags:["'+ tag +'"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0f,0.0625f,0.0625f]},block_state:{Name:"minecraft:'+ id_dict[y][x] +'"}}'

                elif direction == "west":
                    command = 'summon block_display ~'+ str(-1-TINY) +' ~'+ str(coord_y - PIXEL) +' ~'+ str(coord_x) +' {Tags:["'+ tag +'"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0f,0.0625f,0.0625f]},block_state:{Name:"minecraft:'+ id_dict[y][x] +'"}}'


                function_list.append(command)
                if direction == "north" or direction == "east":
                    coord_x -= PIXEL
                elif direction == "south" or direction == "west":
                    coord_x += PIXEL

            coord_y -= PIXEL
            coord_x = 0

        for line in function_list:
            print(line)





    