# author: Ethosa
class ObjType:
    CIRCLE = 0

class Obj:
    def __init__(self, objtype=ObjType.CIRCLE, position=(0, 0), radius=32):
        """
        Creates a new Object
        objtype can be `ObjType.CIRCLE` only.
        position is an object position.
        radius uses for circle
        """
        self.objtype = objtype
        self.position = position

        # object type is CIRCLE
        if objtype == ObjType.CIRCLE:
            self.radius = radius
