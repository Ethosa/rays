from PIL import Image, ImageDraw

from ray import Ray
from objects import Obj, ObjType
from math import pi

TAU = pi*2


class Marcher2D:
    def __init__(self, size=(480, 240), background_color=(33, 33, 33)):
        """
        size is image size
        background_color is an image background color
        """
        self.screen = Image.new('RGBA', size, background_color)
        self.draw = ImageDraw.Draw(self.screen)
        self.objects = [
            Obj.circle((640, 256), 8),
            Obj.circle((640, 64), 64),
            Obj.circle((1024, 0), 128),
            Obj.circle((512, 128), 4)
        ]
        self.fov = 120  # viewing angle

    def look_at(self, camera=(240, 120), angle=90):
        """
        Get look from `camera` point with specific `angle`.
        """
        for current_angle in range(self.fov):
            a = TAU*(((current_angle - self.fov/2) - angle)/360)
            ray = Ray(camera, a, self.objects)
            ray.calculate()
            self.draw.line((camera, ray.point), (222, 222, 222))

        self.screen.show()


if __name__ == '__main__':
    marcher = Marcher2D(size=(1280, 720))
    marcher.look_at(camera=(640, 380))
