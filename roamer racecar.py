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

def findnew(a, b, spread):
    t = []
    for d in [b - 1, b + 1]:
       if a + d * (np.abs(d) + 1) // 2 in range(MARGIN, spread - MARGIN):
           t.append(d)
    if len(t) == 0:
        print("HIBA!!!")
    else:
        d = random.choice(t)
    return d

def update(x, y, u, v):
    u = findnew(x, u, WIDTH)
    v = findnew(y, v, HEIGHT)
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
    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    u1 = 0
    v1 = 0

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        x, y, u, v = draw_window(x, y, u, v)
    pg.quit()
    x, y = 100, 100
    u, v = 10, 10
    print(findnew(54, -10, 1500))


if __name__ == "__main__":
    main()
