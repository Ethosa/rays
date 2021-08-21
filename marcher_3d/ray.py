# author: Ethosa
from objects import ObjType, Obj


class Ray:
    def __init__(self, point=(0, 0, 0), direction=(0, 0, 0), spd=1.0, objects=[], max_steps=25, light_direction=(0, 0, 0)):
        self.objects = objects
        self.spd = spd
        self.direction = direction
        self.point = point
        self.max_steps = 25
        self.shade_color = (0, 0, 0, 0)
        self.bright_color = (255, 255, 255, 0)
        self.is_collided = False
        self.collided_obj = None
        self.light_direction = light_direction

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
                    self.color = obj.albedo_color
                    self.collided_obj = obj
            if spd < self.spd:
                self.is_collided = True
                break

            self.point = (self.point[0] + self.direction[0]*spd, self.point[1] + self.direction[1]*spd, self.point[2] + self.direction[2]*spd)
        if self.collided_obj:
            alpha = round((Obj._distance(self.light_direction, self.direction)*0.65)*255)
            self.shade_color = (0, 0, 0, alpha)
            alpha = round((0.5-Obj._distance(self.light_direction, self.direction))*255)
            self.bright_color = (255, 255, 255, round(alpha*0.2))
