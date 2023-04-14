################
# ROAMER RACECAR

import random
import pygame as pg
import numpy as np

random.seed()

WIDTH, HEIGHT = 1550, 800
LENGTH = 10
MARGIN = LENGTH * (LENGTH + 1) // 2
random.seed()

WIN = pg.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (128, 220, 12)

FPS = 50


def update(x, y, u, v, x1, y1):
    f = np.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    if (f < 26.0):
        x1 = random.randint(MARGIN, WIDTH - MARGIN)
        y1 = random.randint(MARGIN, HEIGHT) - MARGIN
        f = np.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        u = 10.0 * (x1 - x) / f
        v = 10.0 * (y1 - y) / f
    x += u
    y += v
    return x, y, u, v, x1, y1


def draw_window(x, y, u, v, x1, y1):
    WIN.fill(BACKGROUND)
    x, y, u, v, x1, y1 = update(x, y, u, v, x1, y1)
    pg.draw.rect(WIN, (255, 255, 0), ((MARGIN, MARGIN), (WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN)), width=0)
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    pg.display.update()
    return x, y, u, v, x1, y1


def main():
    clock = pg.time.Clock()
    run = True
    x = random.randint(MARGIN, WIDTH - MARGIN)
    y = random.randint(MARGIN, HEIGHT - MARGIN)
    x1 = x + 1
    y1 = y + 1
    u = 0
    v = 0
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        x, y, u, v, x1, y1 = draw_window(x, y, u, v, x1, y1)
    pg.quit()


if __name__ == "__main__":
    main()
