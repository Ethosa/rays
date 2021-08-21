# author: Ethosa
from PIL import Image, ImageDraw
from objects import Obj, ObjType
from ray import Ray


class Marcher3D:
    def __init__(self, size=(720, 480), background_color=(33, 33, 33)):
        self.screen = Image.new('RGB', size, background_color)
        self.draw = ImageDraw.Draw(self.screen, 'RGBA')
        self.size = size
        self.hsize = (size[0]//2, size[1]//2)
        self.ratio = size[1]/size[0]
        self.fov = (size[0]+size[1])*self.ratio
        self.objects = [
            Obj.cube((-5.0, -4.0, -self.fov-15.0), (5.0, 5.0, 10.0), (222, 77, 77, 255)),
            Obj.cube((-4.0, 2.0, -self.fov-30.0), (3, 5, 20), (222, 122, 77, 255)),
            # Obj.sphere((0.0, 0.0, -self.fov-5.0), 1.0, (77, 222, 77, 255)),
            # Obj.sphere((-4.0, -1.0, -self.fov-16.0), 8.0, (222, 77, 77, 255)),
            # Obj.sphere((-1.0, 1.0, -self.fov-7.0), 1.0, (77, 77, 222, 255)),
            Obj.sphere((0.5, -0.5, -self.fov-2.0), 0.7, (222, 77, 222, 255)),
        ]

    def look_at(self, camera=(0.0, 0, 0), light_from=(0.3, 0.2, -0.5)):
        """
        Get look from camera point.
        """
        camera = (camera[0], camera[1], camera[2]-self.fov)
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                direction = Obj._normalize(
                    (self.hsize[0] - x + camera[0], self.hsize[1] - y + camera[1], camera[2])
                )
                ray = Ray(point=camera, direction=direction, objects=self.objects, light_direction=light_from)
                ray.calculate()
                if ray.collided_obj:
                    self.draw.point((x, y), ray.collided_obj.albedo_color)
                    self.draw.point((x, y), ray.shade_color)
                    self.draw.point((x, y), ray.bright_color)
                    self.draw.point((x, y), ray.distance_color)
        self.screen.show()
        self.screen.save('output.png')


if __name__ == '__main__':
    marcher = Marcher3D()
    marcher.look_at()
