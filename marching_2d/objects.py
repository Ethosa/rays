# author: Ethosa
class ObjType:
    CIRCLE = 0

class Obj:
    def circle(point=(0, 0), radius=1.0):
        """
        Creates circle at `point` with `radius`.
        """
        result = Obj()
        result.objtype = ObjType.CIRCLE
        result.radius = radius
        result.point = point
        return result
