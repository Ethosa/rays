# author: Ethosa
from PIL import Image
from objects import Obj, ObjType
from ray import Ray

from math import cos, sin

class Marcher3D:
    def __init__(self, size=(1280, 720), background_color=(33, 33, 33)):
        self.screen = Image.new('RGBA', size, background_color)
        self.size = size
        self.objects = [
            Obj.sphere((0, 0, -64))
        ]
        self.fov = 60

    def _frange(frm, to, step):
        if frm > to:
            while frm > to:
                yield round(frm, 5)
                frm += step
        else:
            while frm < to:
                yield round(frm, 5)
                frm += step


    def look_at(self, eye_point=(0, 0, 0), eye_angle=(0, 0, 0)):
        steps = ((self.size[0]/self.fov)/self.fov,
                 (self.size[1]/self.fov)/self.fov)
        for angle_x in Marcher3D._frange(0, self.fov, steps[0]):
            for angle_y in Marcher3D._frange(0, self.fov, steps[1]):
                direction = (cos(angle_x)+eye_angle[0],  # X
                             sin(angle_x)+eye_angle[1],  # Y
                             cos(angle_y)+eye_angle[2])  # Z
                ray = Ray(point=eye_point, direction=direction, spd=100.0, objects=self.objects)
                ray.calculate()


if __name__ == '__main__':
    marcher = Marcher3D()
    marcher.look_at()
