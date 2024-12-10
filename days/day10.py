import collections

TopoMap = collections.namedtuple('TopoMap',
            ['heights', 'starts', 'ends'])

def parse(inp):
    rows = inp.splitlines()
    tiles = dict()
    starts = set()
    ends = set()
    for y, row in enumerate(rows):
        row = [int(t) for t in row]
        for x, height in enumerate(row):
            if height == 0:
                starts.add((x,y))
            elif height == 9:
                ends.add((x,y))
            tiles[(x,y)] = height

    return TopoMap(tiles, starts, ends)


DIRS = [(1,0),(0,1),(-1,0), (0,-1)]
def neighbors(pos):
    x, y = pos
    for dx, dy in DIRS:
        yield x+dx, y+dy


def part1(topo_map):
    reachable = dict()
    stack = list(zip(topo_map.ends, topo_map.ends))

    while stack:
        curr, src = stack.pop()
        reachable.setdefault(curr, set()).add(src)

        curr_height = topo_map.heights[curr]
        for next in neighbors(curr):
            if next not in topo_map.heights:
                continue
            next_height = topo_map.heights[next]
            if next_height == curr_height-1:
                stack.append((next, src))

    return sum(len(reachable[start]) for start in topo_map.starts)


def part2(topo_map):
    reachable = dict()
    stack = list(zip(topo_map.ends, topo_map.ends))

    while stack:
        curr, src = stack.pop()
        reachable.setdefault(curr, list()).append(src)

        curr_height = topo_map.heights[curr]
        for next in neighbors(curr):
            if next not in topo_map.heights:
                continue
            next_height = topo_map.heights[next]
            if next_height == curr_height-1:
                stack.append((next, src))

    return sum(len(reachable[start]) for start in topo_map.starts)
