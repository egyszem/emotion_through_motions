# Random kör

import random
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw


im = Image.new('L', (Params.width, Params.height))
draw = ImageDraw.Draw(im)

random.seed()

#################
class Roamer2:
    # BUTTERFLY
    def __init__(self):
        self.length = 6
        self.turn = 60
        self.alpha = np.pi / self.turn
        self.radius = int(self.length * self.turn / np.pi / 2.0)
        self.si = np.sin(self.alpha)
        self.co = np.cos(self.alpha)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.u = self.length * self.si
        self.v = self.length * self.co

    def update(self):
        if (int(self.x) in range(2 * self.radius, WIDTH - 2 * self.radius)) and (
                int(self.y) in range(2 * self.radius, HEIGHT - 2 * self.radius)):
            if random.randint(0, 8) == 0:
                self.si = random.choice((1, -1)) * self.si
        a = self.co * self.u - self.si * self.v
        b = self.si * self.u + self.co * self.v
        self.u = a
        self.v = b
        self.x += self.u
        self.y += self.v
        return self.x, self.y
roamer2 = Roamer2()

while True:
    x, y = roamer2.update()
    draw.line((x1, y1, x, y), fill=255, width=2, joints=None)
im.show()