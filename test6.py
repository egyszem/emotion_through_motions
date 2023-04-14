################
# közelítős animáció kép pacával

import random
import pygame as pg
import numpy as np

random.seed()

WIDTH, HEIGHT = 1550, 800

WIN = pg.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (128, 220, 12)

FPS = 50

x, y, x1, y1 = 0, HEIGHT / 2, WIDTH / 2, HEIGHT / 2
u, v, u1, v1 = 0, 0, 0, 0
diff = (x1 - x, y1 - y)
print(diff[0], diff[1])


def update(x, y, u, v, x1, y1, u1, v1, phase):
    global diff
    if phase == 1:
        f = np.sqrt(diff[0] ** 2 + diff[1] ** 2)
        if f > 30:
            x += u
            y += v
    else:
        phase = 2
    if phase == 2:
        u, v = v, -u
        x += u
        y += v
        u, v = np.co * u - np.si * v, np.si * u, np.co * v
    return x, y, u, v, x1, y1, u1, v1

def draw_window(x, y, u, v, x1, y1, u1, v1, phase):
    WIN.fill(BACKGROUND)
    x, y, u, v, x1, y1, u1, v1 = update(x, y, u, v, x1, y1, u1, v1, phase)
    pg.draw.rect(WIN, (255, 255, 0), ((RADIUS, RADIUS), (WIDTH - 2 * RADIUS, HEIGHT - 2 * RADIUS)), width=0)
    pg.draw.circle(WIN, (0, 0, 0), (x, y), width=0, radius=20)
    pg.draw.circle(WIN, (0, 0, 255), (x1, y1), width=0, radius=20)
    pg.display.update()
    return x, y, u, v, x1, y1, u1, v1


def main():
    clock = pg.time.Clock()
    run = True
    phase = 1
    f = np.sqrt(diff[0] ** 2 + diff[1] ** 2)
    len = 5
    alpha = np.pi / 20
    si = np.sin(alpha)
    co = np.cos(alpha)
    u = 5 * diff[0] / f
    v = 0 * diff[1] / f

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        x, y, u, v, x1, y1, u1, v1 = draw_window(x, y, u, v, x1, y1, u1, v1, phase)
    pg.quit()

if __name__ == "__main__":
    main()
