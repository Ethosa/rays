# author: Ethosa
from objects import ObjType, Obj


class Ray:
    def __init__(self, point=(0, 0, 0), direction=(0, 0, 0), spd=1.0, objects=[], max_steps=25):
        self.objects = objects
        self.spd = spd
        self.direction = direction
        self.point = point
        self.max_steps = 25

    def _get_valide_length(self, obj):
        length = self.spd
        while obj.is_collide(self.point + self.direction*length) or length > 0.1:
            length /= 2.0
        return length

    def calculate(self):
        for i in range(self.max_steps):
            is_collide = False
            length = self.spd
            for obj in self.objects:
                pass
