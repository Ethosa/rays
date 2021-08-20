# author: Ethosa
from math import sqrt


class ObjType:
    SPHERE = 0


class Obj:
    def sphere(position=(0, 0, 0), radius=32.0):
        obj = Obj()
        obj.objtype = ObjType.SPHERE
        obj.position = position
        obj.radius = radius
        return obj

    def is_collide(self, point):
        if self.objtype == ObjType.SPHERE:
            return _distance(self.position, point) < self.radius

    def _distance(pnt1, pnt2):
        return sqrt((pnt2[0]-pnt1[0])**2 + (pnt2[1]-pnt1[1])**2 + (pnt2[2]-pnt1[2])**2)
