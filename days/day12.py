
DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
def neighbors(pos):
    x, y = pos
    for dx,dy in DIRS:
        yield x+dx, y+dy


def get_regions(plots):
    unvisited = plots.copy()
    while unvisited:
        region = set()
        curr = unvisited.pop()
        stack = [curr]
        while stack:
            curr = stack.pop()
            region.add(curr)
            for nxt in neighbors(curr):
                if nxt in unvisited:
                    unvisited.remove(nxt)
                    stack.append(nxt)
        yield region


def parse(inp):
    farm = dict()
    for y, row in enumerate(inp.splitlines()):
        for x, plant in enumerate(row):
            farm.setdefault(plant, set()).add((x,y))

    regions = []
    for plant, plots in farm.items():
        regions.extend(get_regions(plots))
    return regions


def count_perimeter(region):
    perimeter = 0
    for plot in region:
        for nxt in neighbors(plot):
            if nxt not in region:
                perimeter += 1
    return perimeter


def part1(regions):
    price = 0
    for region in regions:
        price += len(region) * count_perimeter(region)
    return price


CORNERS = [((1,0),(0,1),(1,1)), ((0,1),(-1,0), (-1,1)),
           ((-1,0),(0,-1),(-1,-1)), ((0,-1),(1,0),(1,-1))]
def corners(pos):
    x, y = pos
    for corner in CORNERS:
        nxt = [(x+dx, y+dy) for (dx,dy) in corner]
        yield nxt


def count_sides(region):
    # corner count is equal to side count
    sides = 0
    for plot in region:
        for corner in corners(plot):
            a,b,c = corner
            # Outer corner
            sides += a not in region and b not in region
            # Inner corner
            sides += a in region and b in region and c not in region
    return sides


def part2(regions):
    price = 0
    for region in regions:
        price += len(region) * count_sides(region)
    return price



