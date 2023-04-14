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


def update(x, y, u, v):
    f = np.sqrt((x - 0.5 * WIDTH) ** 2 + (y - 0.5 * HEIGHT) ** 2) ** 1.3
    coeff = 1.2
    u += coeff * (0.5 * WIDTH - x) / f
    v += coeff * (0.5 * HEIGHT - y) / f
    x += u
    y += v
    return x, y, u, v


def draw_window(x, y, u, v):
    WIN.fill(BACKGROUND)
    x, y, u, v = update(x, y, u, v)
    pg.draw.rect(WIN, (255, 255, 0), ((MARGIN, MARGIN), (WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN)), width=0)
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    pg.display.update()
    return x, y, u, v


def main():
    clock = pg.time.Clock()
    run = True
    x = random.randint(MARGIN, WIDTH - MARGIN)
    y = random.randint(MARGIN, HEIGHT - MARGIN)
    u = random.randint(-5, 5)
    v = random.randint(-5, 5)
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        x, y, u, v = draw_window(x, y, u, v)
    pg.quit()


if __name__ == "__main__":
    main()
