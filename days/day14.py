import itertools
import math
import re

w, h = 101, 103

def parse(inp):
    pos = []
    vel = []
    robot_pattern = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')

    for line in inp.splitlines():
        vals = robot_pattern.match(line)
        x,y,vx,vy = map(int, vals.groups())
        pos.append((x,y))
        vel.append((vx,vy))
    return pos, vel


def move_robots(pos, vel):
    new_pos = []
    for (x,y), (vx,vy) in zip(pos, vel):
        nx = (x+vx) % w
        ny = (y+vy) % h
        new_pos.append((nx, ny))
    return new_pos


def part1(robots):
    pos, vel = robots
    for _ in range(100):
        pos = move_robots(pos, vel)

    mw, mh = w // 2, h // 2
    quadrants = [0,0,0,0]
    for (x,y) in pos:
        if x == mw or y == mh:
            continue
        q = 2*(y>mh) + (x>mw)
        quadrants[q] += 1

    return math.prod(quadrants)


def debug_robots(pos):
    pos = set(pos)
    for y in range(h):
        line = []
        for x in range(w):
            c = '#' if (x,y) in pos else ' '
            line.append(c)
        print(f'{y:03d}' + ''.join(line))


def part2(robots):
    pos, vel = robots
    len_pos = len(pos)

    # Picture appears when all robots are at unique location
    for i in itertools.count(1):
        pos = move_robots(pos, vel)
        if len(set(pos)) == len_pos:
            break
    return i
