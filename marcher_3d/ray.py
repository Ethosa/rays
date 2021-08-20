# author: Ethosa
from objects import ObjType, Obj


class Ray:
    def __init__(self, point=(0, 0, 0), direction=(0, 0, 0), spd=1.0, objects=[], max_steps=25):
        self.objects = objects
        self.spd = spd
        self.direction = direction
        self.point = point
        self.max_steps = 25
        self.ideal = (point[0]+(direction[0]*spd)*self.max_steps,
                      point[0]+(direction[1]*spd)*self.max_steps,
                      point[0]+(direction[2]*spd)*self.max_steps)

    def _add_points(pnt1, pnt2):
        return (pnt1[0] + pnt2[0], pnt1[1] + pnt2[1], pnt1[1] + pnt2[1])

    def _add_num_to_point(pnt, num):
        return (pnt[0] + num, pnt[1] + num, pnt[1] + num)

    def _get_valide_length(self, obj):
        length = Obj._distance(obj.point, self.point)-1.0
        while obj.is_collide(Ray._add_num_to_point(Ray._add_points(self.point,self.direction), length)) and length > 0.1:
            length /= 2.0
        return length

    def calculate(self):
        for i in range(self.max_steps):
            is_collide = False
            spd = self.spd
            for obj in self.objects:
                if obj.is_collide(self.point):
                    spd = self._get_valide_length(obj)

            self.point = (self.point[0] + self.direction[0]*spd, self.point[1] + self.direction[1]*spd, self.point[2] + self.direction[2]*spd)

    def is_not_collided(self):
        return self.point == self.idel
