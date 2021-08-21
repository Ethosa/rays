# author: Ethosa
from PIL import Image
from objects import Obj, ObjType
from ray import Ray

from math import cos, sin

class Marcher3D:
    def __init__(self, size=(256, 256), background_color=(33, 33, 33)):
        self.screen = Image.new('RGBA', size, background_color)
        self.size = size
        self.hsize = (size[0]//2, size[1]//2)
        self.objects = [
            Obj.sphere((0.0, 0.0, -64.0), 1.0, (222, 77, 222)),
            Obj.sphere((5.0, 0.0, -64.0), 1.0, (77, 77, 222)),
            Obj.sphere((4.0, -4.0, -64.0), 1.0, (222, 77, 77)),
        ]

    def look_at(self, camera=(0, 0, -60.0)):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                direction = Obj._normalize(
                    (self.hsize[0] - x + camera[0], self.hsize[1] - y + camera[1], 0 + camera[2])
                )
                ray = Ray(point=camera, direction=direction, objects=self.objects)
                ray.calculate()
                if ray.is_collided:
                    self.screen.putpixel((x, y), ray.collided_obj.albedo_color)
        self.screen.show()


if __name__ == '__main__':
    marcher = Marcher3D()
    marcher.look_at()
