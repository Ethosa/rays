# author: Ethosa
from PIL import Image, ImageDraw
from objects import Obj, ObjType
from ray import Ray

from math import cos, sin

class Marcher3D:
    def __init__(self, size=(480, 360), background_color=(33, 33, 33)):
        self.screen = Image.new('RGB', size, background_color)
        self.draw = ImageDraw.Draw(self.screen, 'RGBA')
        self.size = size
        self.hsize = (size[0]//2, size[1]//2)
        self.objects = [
            Obj.sphere((0.0, 0.0, -61.0), 1.0, (77, 222, 77, 255)),
        ]

    def look_at(self, camera=(0, 0, -60.0), light_from=(-0.5, 0.4, -0.8)):
        """
        Get look from camera point.
        """
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                direction = Obj._normalize(
                    (self.hsize[0] - x + camera[0], self.hsize[1] - y + camera[1], 0 + camera[2])
                )
                ray = Ray(point=camera, direction=direction, objects=self.objects, light_direction=light_from)
                ray.calculate()
                if ray.is_collided:
                    self.draw.point((x, y), ray.collided_obj.albedo_color)
                    self.draw.point((x, y), ray.shade_color)
                    self.draw.point((x, y), ray.bright_color)
        self.screen.show()


if __name__ == '__main__':
    marcher = Marcher3D()
    marcher.look_at()
