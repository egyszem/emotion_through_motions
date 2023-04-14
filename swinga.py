################
# inga

import sys
import random
import pygame as pg
import numpy as np
from PIL import Image, ImageDraw

random.seed()

WIDTH, HEIGHT = 1500, 1500
LENGTH = 20

WIN = pg.display.set_mode((WIDTH, HEIGHT))
IM = Image.new('P', (WIDTH, HEIGHT))
IM.save('swing.png')
IM = Image.open('swing.png')
DRAW = ImageDraw.Draw(IM)

BACKGROUND = (128, 220, 12)

FPS = 20


class Swing:
    global WIDTH, HEIGHT

    def __init__(self, x=WIDTH / 4, y=HEIGHT / 4):
        self.length = 10
        self.margin = self.length * (self.length + 1) // 2
        self.x = x  # random.randint(self.margin, WIDTH - self.margin)
        self.y = y  # random.randint(self.margin, HEIGHT - self.margin)
        self.u = 0.05 * (self.y - HEIGHT / 2)  # random.randint(-5, 5)
        self.v = -0.05 * (self.x - WIDTH / 2)  # random.randint(-5, 5)
        self.beta_0 = 0.999
        self.beta = 0.3
        print(self.u, self.v)

    def update(self):
        f = np.sqrt((self.x - 0.5 * WIDTH) ** 2 + (self.y - 0.5 * HEIGHT) ** 2) ** 1.3
        coeff = 8
        # self.beta *= self.beta_0
        self.u += coeff * (0.5 * WIDTH - self.x) / f
        self.v += coeff * (0.5 * HEIGHT - self.y) / f
        self.x += self.beta * self.u
        self.y += self.beta * self.v
        return self.x, self.y


global pos_list
# pos_list = []
pos_list = (WIDTH / 4 + 10, HEIGHT / 2 + 10)
swing = Swing(x=pos_list[0], y=pos_list[1])


def draw_window():
    # WIN.fill(BACKGROUND)
    global pos_list
    x0, y0 = pos_list
    x, y, = swing.update()
    colour = np.array([255, 255, 255])
    # pg.draw.circle(WIN, colour, (x, y), width=0, radius=3)
    pg.draw.line(WIN, colour, (x, y), (x0, y0), width=1)
    DRAW.line((x, y, x0, y0), fill=tuple(colour), width=1)
    pos_list = (x, y)
    # pos_list.append((x, y))
    # for i in range(len(pos_list)):
    #     xx, yy = pos_list[i]
    #     pg.draw.circle(WIN, colour * i / len(pos_list), (xx, yy), width=0, radius=3)
    pg.display.update()


def main():
    clock = pg.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        draw_window()
    pg.quit()
    st = sys.stdout
    IM.save("swing" + str(random.randint(0, 100)) + ".png")
    # IM = Image.open(st + '.png')
    # IM.show()


if __name__ == "__main__":
    main()
