# author: Ethosa
from math import sqrt


class ObjType:
    SPHERE = 0


class Obj:
    def sphere(point=(0, 0, 0), radius=32.0, albedo_color=(0, 0, 0)):
        obj = Obj()
        obj.objtype = ObjType.SPHERE
        obj.point = point
        obj.radius = radius
        obj.albedo_color = albedo_color
        return obj

    def is_collide(self, point):
        if self.objtype == ObjType.SPHERE:
            return Obj._distance(self.point, point) < self.radius

    def _direction(pnt1, pnt2):
        result = Obj._normalize((pnt1[0] - pnt2[0], pnt1[1] - pnt2[1], pnt1[1] - pnt2[1]))
        return result

    def _distance(pnt1, pnt2):
        return sqrt((pnt2[0]-pnt1[0])**2 + (pnt2[1]-pnt1[1])**2 + (pnt2[2]-pnt1[2])**2)

    def _normalize(pnt):
        l = Obj._distance((0, 0, 0), pnt)
        if l != 0.0:
            return (pnt[0] / l, pnt[1] / l, pnt[2] / l)
        return (0.0, 0.0, 0.0)
