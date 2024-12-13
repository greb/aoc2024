import re

def parse(inp):
    parse_line = lambda l: tuple(int(n) for n in re.findall(r'\d+', l))
    machines = []
    for lines in inp.split('\n\n'):
        a, b, p = map(parse_line, lines.splitlines())
        machines.append((a,b,p))
    return machines


def part1(machines):
    total = 0
    for machine in machines:
        (xa,ya), (xb,yb), (xp, yp) = machine
        for nb in range(100, 0, -1):
            rx = xp - nb*xb
            ry = yp - nb*yb
            if rx < 0 or ry < 0:
                continue
            na1, xm = divmod(rx, xa)
            na2, ym = divmod(ry, ya)
            if xm != 0 or ym != 0:
                continue
            if  na1 != na2:
                continue
            total += nb + na1*3
    return total


ADD = 10000000000000
def part2(machines):
    total = 0
    for machine in machines:
        (xa,ya), (xb,yb), (xp, yp) = machine
        na, r = divmod(((xp+ADD)*yb - (yp+ADD)*xb), (xa*yb - ya*xb))
        if r != 0:
            continue
        nb = ((xp+ADD) - (na*xa)) // xb
        total += nb + 3*na

    return total
