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
            Obj(position=(640, 256), radius=8),
            Obj(position=(640, 64), radius=64),
            Obj(position=(1024, 0), radius=128),
            Obj(position=(512, 128), radius=4)
        ]
        self.fov = 120  # viewing angle

    def cast(self, eye=(240, 120), angle=90):
        """
        Cast rays from `eye` position with specific `angle`
        """
        for current_angle in range(self.fov):
            a = TAU*(((current_angle - self.fov/2) - angle)/360)
            ray = Ray(eye, a, self.objects)
            ray.calculate()
            self.draw.line((eye, ray.positions[-1]), (222, 222, 222))

        self.screen.show()


if __name__ == '__main__':
    marcher = Marcher2D(size=(1280, 720))
    marcher.cast(eye=(640, 380))
