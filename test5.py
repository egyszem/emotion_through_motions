################
# AZ ELSŐ VALAMENNYIRE MŰKÖDŐ "FÉLŐS" ANIMÁCIÓ KÉT RANDOM PACA KÖZT

import random
import pygame as pg
import numpy as np

random.seed()

WIDTH, HEIGHT = 1550, 800
LENGTH = 10
TURN = 60
ALPHA = np.pi / TURN
RADIUS = int(LENGTH * TURN / np.pi / 2.0)
print("RADIUS", RADIUS)
SI = np.sin(ALPHA)
CO = np.cos(ALPHA)
WIN = pg.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (128, 220, 12)

FPS = 50

class Spot:
    def __init__(self, x, y, u, v, x1, y1, u1, v1, color, size):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.x1 = x1
        self.y1 = y1
        self.u1 = u1
        self.v1 = v1
        self.color = color
        self.size = size

    def attract(coeff, x, y, x1, y1, power):
        return coeff * np.exp((x - x1) * (x - x1) + (y - y1) * (y - y1), 0.5 * power)

    def update(x, y, u, v):
        u = Spot.attract(1e3, x, y, x1, y1, 2.6) * (x1 - x)
        v = Spot.attract(1e3, x, y, x1, y1, 2.6) * (y1 - y)
        x += u
        y += v
        return(x, y, u, v)




def update(x, y, u, v, x1, y1, u1, v1):
    global SI, CO
    coeff = 1e3 / (((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 1.3)
    coeff2 = 5 * 1e-1
    if (int(x) in range (2 * RADIUS, WIDTH - 2 * RADIUS)) and (int(y) in range (2 * RADIUS, HEIGHT - 2 * RADIUS)):
        if random.randint(0, 8) == 0:
            SI = random.choice((SI, -SI))
    u, v = CO * u - SI * v - 1e-10 * coeff * (x1 - x), SI * u + CO * v - 1e-10 * coeff * (y1 - y)
    x += u
    y += v
    u1 = 1e3 * coeff * (x1 - x) + coeff2 * (WIDTH // 2 - x1)
    v1 = 1e3 * coeff * (y1 - y) + coeff2 * (HEIGHT // 2 - y1)
    # A KÉK FÉL A FEKETÉTŐL ÉS VALAMENNYIRE VISSZAVÁGYIK KÖZÉPRE
    x1 += u1
    y1 += v1
    return x, y, u, v, x1, y1, u1, v1

def draw_window(x, y, u, v, x1, y1, u1, v1):
    WIN.fill(BACKGROUND)
    x, y, u, v, x1, y1, u1, v1 = update(x, y, u, v, x1, y1, u1, v1)
    pg.draw.rect(WIN, (255, 255, 0), ((RADIUS, RADIUS), (WIDTH - 2 * RADIUS, HEIGHT - 2 * RADIUS)), width=0)
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    pg.draw.circle(WIN, (0, 0, 255), (x1, y1), width=0, radius=20)
    pg.display.update()
    return x, y, u, v, x1, y1, u1, v1


def main():
    clock = pg.time.Clock()
    run = True
    x = random.randint(RADIUS, WIDTH - RADIUS)
    y = random.randint(RADIUS, HEIGHT - RADIUS)
    u = random.randint(-5, 5)
    v = random.randint(-5, 5)
    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    u1 = 0
    v1 = 0

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        x, y, u, v, x1, y1, u1, v1 = draw_window(x, y, u, v, x1, y1, u1, v1)
    pg.quit()
    x, y = 100, 100
    u, v = 10, 10

if __name__ == "__main__":
    main()
