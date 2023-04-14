################
# BOLYONGÓ

import random
import pygame as pg
import numpy as np

random.seed()

WIDTH, HEIGHT = 1550, 800
LENGTH = 20

WIN = pg.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (128, 220, 12)

FPS = 20


class Roamer1:
    # RACECAR
    global WIDTH, HEIGHT

    def __init__(self):
        self.length = 10
        self.margin = self.length * (self.length + 1) // 2
        self.x = random.randint(self.margin, WIDTH - self.margin)
        self.y = random.randint(self.margin, HEIGHT - self.margin)
        self.u = random.randint(-5, 5)
        self.v = random.randint(-5, 5)

    def update(self):
        def findnew(a, b, margin, spread):
            t = []
            for d in [b - 1, b + 1]:
                if a + d * (np.abs(d) + 1) // 2 in range(margin, spread):
                    t.append(d)
            if len(t) == 0:
                print("HIBA!!!")
            else:
                d = random.choice(t)
            return d

        self.u = findnew(self.x, self.u, self.margin, WIDTH - 2 * self.margin)
        self.v = findnew(self.y, self.v, self.margin, HEIGHT - 2 * self.margin)
        self.x += self.u
        self.y += self.v
        return self.x, self.y

class Roamer2:
    # BUTTERFLY
    def __init__(self):
        self.length = 6
        self.turn = 60
        self.alpha = np.pi / self.turn
        self.radius = 2 * int(self.length * self.turn / np.pi / 2.0)
        self.si = np.sin(self.alpha)
        self.co = np.cos(self.alpha)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.u = self.length * self.si
        self.v = self.length * self.co
        print(self.radius)

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

class Roamer3:
    # FLY
    global WIDTH, HEIGHT

    def __init__(self):
        self.length = 10
        self.margin = self.length * (self.length + 1) // 2
        self.x = random.randint(self.margin, WIDTH - self.margin)
        self.y = random.randint(self.margin, HEIGHT - self.margin)
        self.x1 = self.x + 1
        self.y1 = self.y + 1
        self.u = 0
        self.v = 0

    def update(self):
        f = np.sqrt((self.x - self.x1) ** 2 + (self.y - self.y1) ** 2)
        if (f < 26.0):
            self.x1 = random.randint(self.margin, WIDTH - self.margin)
            self.y1 = random.randint(self.margin, HEIGHT) - self.margin
            f = np.sqrt((self.x - self.x1) ** 2 + (self.y - self.y1) ** 2)
            self.u = 10.0 * (self.x1 - self.x) / f
            self.v = 10.0 * (self.y1 - self.y) / f
        self.x += self.u
        self.y += self.v
        return self.x, self.y

class Roamer4:
    # ATTRACTED
    global WIDTH, HEIGHT

    def __init__(self):
        self.length = 10
        self.margin = self.length * (self.length + 1) // 2
        self.x = WIDTH / 4 #random.randint(self.margin, WIDTH - self.margin)
        self.y = HEIGHT / 4 #random.randint(self.margin, HEIGHT - self.margin)
        self.u = -0.01 * (self.y - HEIGHT / 2) # random.randint(-5, 5)
        self.v = -0.01 * (self.x - WIDTH / 2) # random.randint(-5, 5)
        self.beta_0 = 0.999
        self.beta = 1
        print(self.u, self.v)

    def update(self):
        f = np.sqrt((self.x - 0.5 * WIDTH) ** 2 + (self.y - 0.5 * HEIGHT) ** 2) ** 1.3
        coeff = 3.8
        # self.beta *= self.beta_0
        self.u += coeff * (0.5 * WIDTH - self.x) / f
        self.v += coeff * (0.5 * HEIGHT - self.y) / f
        self.x += self.beta * self.u
        self.y += self.beta * self.v
        return self.x, self.y


roamer1 = Roamer1()

roamer2 = Roamer2()

roamer3 = Roamer3()

roamer4 = Roamer4()

def update():

    x1, y1 = roamer1.update()
    x2, y2 = roamer2.update()
    x3, y3 = roamer3.update()
    x4, y4 = roamer4.update()
    return x1, y1, x2, y2, x3, y3, x4, y4

def draw_window():
    WIN.fill(BACKGROUND)
    x1, y1, x2, y2, x3, y3, x4, y4 = update()
    r = roamer2.radius
    pg.draw.rect(WIN, (255, 255, 0), ((r, r), (WIDTH - 2 * r, HEIGHT - 2 * r)), width=0)
    x, y = roamer1.update()
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    x, y = roamer2.update()
    pg.draw.circle(WIN, (128, 255, 0), (x, y), width=0, radius=20)
    x, y, = roamer3.update()
    pg.draw.circle(WIN, (0, 128, 255), (x, y), width=0, radius=20)
    x, y, = roamer4.update()
    pg.draw.circle(WIN, (255, 0, 255), (x, y), width=0, radius=20)
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


if __name__ == "__main__":
    main()
