import pygame


class VECTOR:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class QUAD:
    def __init__(self,x,y,w,h) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h

        self.position = VECTOR(x,y)
        self.size = VECTOR(w,h)

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
    object.x += movement.x
    hit_list = collision_test(object)

    # if the object collided 
    for tile in hit_list:

        # if was moving right 
        if movement.x > 0:
            object.right = tile.left
            collision_type["right"] = True

        #if was moving left
        elif movement.x < 0:
            object.left = tile.right
            collision_type["left"] = True

    #Check for vertical movement
    object.y += movement.y
    hit_list = collision_test(object)

    #if collides
    for tile in hit_list:
        # if collided with floor
        if movement.y > 0:
            object.bottom = tile.top
            collision_type["bottom"] = True
        #if collided with ceil
        elif movement.y < 0:
            object.top = tile.bottom
            collision_type["top"] = True

    return object, collision_type


def distance(obj1:VECTOR, obj2:VECTOR) -> VECTOR:
    return VECTOR( obj2.x-obj1.x, obj2.y-obj1.y)

def dot(obj1:VECTOR, obj2:VECTOR) -> int:
    return int((obj1.x)(obj2.x)+(obj1.y)(obj2.y))