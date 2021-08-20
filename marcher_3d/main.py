# author: Ethosa
from PIL import Image
from objects import Obj, ObjType
from ray import Ray


class Marcher3D:
    def __init__(self, size=(1280, 720), background_color=(33, 33, 33)):
        self.screen = Image.new('RGBA', size, background_color)
        self.size = size
        self.objects = [
            Obj.sphere((0, 0, -64))
        ]


    def look_at(self, eye_point=(0, 0, 0), eye_angle=(0, 0, 0)):
        pass

if __name__ == '__main__':
    marcher = Marcher3D()
    marcher.look_at()
