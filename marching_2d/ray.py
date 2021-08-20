# author: Ethosa
from objects import ObjType
from math import sqrt, sin, cos

v = 2**16


class Ray:
    def __init__(self, pos, angle, objs):
        self.positions = [pos]
        self.objs = objs
        self.min_length = v
        self.direction = (cos(angle), sin(angle))
        self.max_steps = 750

    def go(self, step):
        """
        Goes in specific direction
        """
        self.positions.append((self.positions[-1][0] + self.direction[0]*step, self.positions[-1][1] + self.direction[1]*step))

    def calculate(self):
        step = 0
        while self.min_length > 0.0 and step < self.max_steps:
            self.min_length = v
            collide = False

            for obj in self.objs:
                tmp_length, tmp_collide = self._calc_length_to(obj)
                if tmp_collide:
                    collide = True
                if tmp_length < self.min_length:
                    self.min_length = 1.0

            if self.min_length > v/2 or collide:
                break

            self.go(self.min_length)
            step += 1

    def _calc_length_to(self, obj):
        """
        Returns (length, is_collide)
        length is a distance between the ray's current position and the object.
        is_collide is True when a ray collides with the object.
        """
        if obj.objtype == ObjType.CIRCLE:
            length = sqrt((obj.position[0]-self.positions[-1][0])**2 + (obj.position[1]-self.positions[-1][1])**2)
            return length, length <= obj.radius
