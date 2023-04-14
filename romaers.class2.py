################
# BOLYONGÓ

import random
import pygame as pg
import numpy as np

random.seed()

WIDTH, HEIGHT = 1550, 800
LENGTH = 10
LENGTH = 6
MARGIN = LENGTH * (LENGTH + 1) // 2
TURN = 60
ALPHA = np.pi / TURN
CO = LENGTH * np.cos(ALPHA)
SI = LENGTH * np.sin(ALPHA)
RADIUS = 2 * int(LENGTH * TURN / np.pi / 2.0)
WIN = pg.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (128, 220, 12)

FPS = 20

class Roamer:
    global WIDTH, HEIGHT, LENGTH, MARGIN, TURN, ALPHA, CO, SI, RADIUS

    def __init__(self, x, y, u, v):
        self.si = SI
        self.co = CO
        self.x = x
        self.y = y
        self.u = u
        self.v = v

    def modify(self):
        if (int(self.x) in range(2 * RADIUS, WIDTH - 2 * RADIUS)) and (
                int(self.y) in range(2 * RADIUS, HEIGHT - 2 * RADIUS)):
            if random.randint(0, 8) == 0:
                self.si = random.choice((1, -1)) * self.si
        self.u, self.v = self.co * self.u - self.si * self.v, self.si * self.u + self.co * self.v

    def update(self):
        self.modify()
        self.x += self.u
        self.y += self.v
        return self.x, self.y

class Roamer1(Roamer):
# RACECAR
    def modify(self):
        def findnew(a, b, spread):
            t = []
            for d in [b - 1, b + 1]:
                if a + d * (np.abs(d) + 1) // 2 in range(MARGIN, spread):
                    t.append(d)
            if len(t) == 0:
                print("HIBA!!!")
            else:
                d = random.choice(t)
            print(b, MARGIN, spread, t, d)
            return d

        self.u = findnew(self.x, self.u, WIDTH - 2 * MARGIN)
        self.v = findnew(self.y, self.v, HEIGHT - 2 * MARGIN)

class Roamer2(Roamer):
    # BUTTERFLY
    def modify(self):
        if (int(self.x) in range(2 * RADIUS, WIDTH - 2 * RADIUS)) and (
                int(self.y) in range(2 * RADIUS, HEIGHT - 2 * RADIUS)):
            if random.randint(0, 8) == 0:
                self.si = random.choice((1, -1)) * self.si
        self.u, self.v = self.co * self.u - self.si * self.v, self.si * self.u + self.co * self.v

class Roamer3(Roamer):
    # FLY

    def modify(self):
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
        self.x = random.randint(self.margin, WIDTH - self.margin)
        self.y = random.randint(self.margin, HEIGHT - self.margin)
        self.x1 = self.x + 1
        self.y1 = self.y + 1
        self.u = random.randint(-5, 5)
        self.v = random.randint(-5, 5)
        print(self.u, self.v)

    def update(self):
        f = np.sqrt((self.x - 0.5 * WIDTH) ** 2 + (self.y - 0.5 * HEIGHT) ** 2) ** 1.3
        coeff = 3.8
        self.u += coeff * (0.5 * WIDTH - self.x) / f
        self.v += coeff * (0.5 * HEIGHT - self.y) / f
        self.x += self.u
        self.y += self.v
        return self.x, self.y


roamer1 = Roamer1(WIDTH // 2, HEIGHT // 2, random.randint(-5, 5), random.randint(-5, 5))

roamer2 = Roamer2(WIDTH // 2, HEIGHT // 2, int(LENGTH * CO), int(LENGTH * SI))

roamer3 = Roamer3(random.randint(MARGIN, WIDTH - MARGIN), random.randint(MARGIN, HEIGHT - MARGIN), 0, 0)

#roamer4 = Roamer4()

def update():

    x1, y1 = roamer1.update()
    x2, y2 = roamer2.update()
    # x3, y3 = roamer3.update()
    # x4, y4 = roamer4.update()
    return x1, y1, x2, y2 #, x3, y3, x4, y4

def draw_window():
    WIN.fill(BACKGROUND)
    update()
    pg.draw.rect(WIN, (255, 255, 0), ((RADIUS, RADIUS), (WIDTH - 2 * RADIUS, HEIGHT - 2 * RADIUS)), width=0)
    x, y = roamer1.update()
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    x, y = roamer2.update()
    pg.draw.circle(WIN, (128, 255, 0), (x, y), width=0, radius=20)
    x, y, = roamer3.update()
    pg.draw.circle(WIN, (0, 128, 255), (x, y), width=0, radius=20)
    # x, y, = roamer4.update()
    # pg.draw.circle(WIN, (255, 0, 255), (x, y), width=0, radius=20)
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
