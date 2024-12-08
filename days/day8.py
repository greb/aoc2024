import itertools

def parse(inp):
    antennas = dict()

    rows = inp.splitlines()
    w,h = len(rows[0]), len(rows)
    for y, row in enumerate(rows):
        for x, tile in enumerate(row):
            if tile != '.':
                antennas.setdefault(tile, list()).append((x,y))
    return w,h,antennas


def part1(inp):
    w, h, antennas = inp
    antinodes = set()
    for name, coords in antennas.items():
        for a,b in itertools.combinations(coords, 2):
            dx,dy = b[0]-a[0], b[1]-a[1]

            x,y = a[0]-dx, a[1]-dy
            if 0 <= x < w and 0 <= y < h:
                antinodes.add((x,y))

            x,y = b[0]+dx, b[1]+dy
            if 0 <= x < w and 0 <= y < h:
                antinodes.add((x,y))
    return len(antinodes)


def part2(inp):
    w, h, antennas = inp
    antinodes = set()
    for name, coords in antennas.items():
        for a,b in itertools.combinations(coords, 2):
            dx, dy = b[0]-a[0], b[1]-a[1]

            x, y = a
            while 0 <= x < w and 0 <= y < h:
                antinodes.add((x,y))
                x,y = x-dx, y-dy

            x, y = b
            while 0 <= x < w and 0 <= y < h:
                antinodes.add((x,y))
                x,y = x+dx, y+dy
    return len(antinodes)
