################
# ROAMER BUTTERFLY

import random
import pygame as pg
import numpy as np

random.seed()

WIDTH, HEIGHT = 1550, 800
LENGTH = 10
TURN = 60
ALPHA = np.pi / TURN
RADIUS = int(LENGTH * TURN / np.pi / 2.0)
SI = np.sin(ALPHA)
CO = np.cos(ALPHA)
WIN = pg.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (128, 220, 12)

FPS = 50

def update(x, y, u, v):
    global SI, CO
    if (int(x) in range (2 * RADIUS, WIDTH - 2 * RADIUS)) and (int(y) in range (2 * RADIUS, HEIGHT - 2 * RADIUS)):
        if random.randint(0, 8) == 0:
            SI = random.choice((SI, -SI))
    u, v = CO * u - SI * v, SI * u + CO * v
    x += u
    y += v
    return x, y, u, v

def draw_window(x, y, u, v):
    WIN.fill(BACKGROUND)
    x, y, u, v = update(x, y, u, v)
    pg.draw.rect(WIN, (255, 255, 0), ((RADIUS, RADIUS), (WIDTH - 2 * RADIUS, HEIGHT - 2 * RADIUS)), width=0)
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    pg.display.update()
    return x, y, u, v


def main():
    clock = pg.time.Clock()
    run = True
    x = random.randint(RADIUS, WIDTH - RADIUS)
    y = random.randint(RADIUS, HEIGHT - RADIUS)
    u = random.randint(-5, 5)
    v = random.randint(-5, 5)


    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        x, y, u, v = draw_window(x, y, u, v)
    pg.quit()
    x, y = 100, 100
    u, v = 10, 10

if __name__ == "__main__":
    main()
