import pygame

collidable_tile_rects = []


def collision_test(object):
    """
    Detects collision for the given object with the map colliders
    """
    hit_list = []
    for tile in collidable_tile_rects:
        if object.colliderect(tile):
            hit_list.append(tile)  # add rects to which the object has collided with
    return hit_list


def move(object: pygame.Rect, movement):
    """
    :object(pygame.Rect): the object which is moving/wants to move
    :movement[x,y]: the amount of pixels it want to move per frame
    :tiles[(Rect1),(Rect2),...]: possible tiles it can collide with
    """
    collision_type = {
        "top": False,
        "bottom": False,
        "left": False,
        "right": False
    }

    # Check for horizontal movement
    object.x += movement[0]
    hit_list = collision_test(object)

    # if the object collided 
    for tile in hit_list:

        # if was moving right 
        if movement[0] > 0:
            object.right = tile.left
            collision_type["right"] = True

        #if was moving left
        elif movement[0] < 0:
            object.left = tile.right
            collision_type["left"] = True

    #Check for vertical movement
    object.y += movement[1]
    hit_list = collision_test(object)

    #if collides
    for tile in hit_list:
        # if collided with floor
        if movement[1] > 0:
            object.bottom = tile.top
            collision_type["bottom"] = True
        #if collided with ceil
        elif movement[1] < 0:
            object.top = tile.bottom
            collision_type["top"] = True

    return object, collision_type
