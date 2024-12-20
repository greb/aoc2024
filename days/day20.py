import collections
import itertools

def parse(inp):
    walls = set()
    for y, row in enumerate(inp.splitlines()):
        for x,c in enumerate(row):
            match c:
                case 'S':
                    start = x,y
                case '#':
                    walls.add((x,y))

    dist = {start: 0}
    queue = collections.deque([start])
    while queue:
        curr = queue.popleft()
        for nxt in neighbors(curr):
            if nxt in walls or nxt in dist:
                continue
            dist[nxt] = dist[curr] + 1
            queue.append(nxt)

    return dist

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
def neighbors(pos):
    for dir in DIRS:
        yield tuple(p+d for p,d in zip(pos, dir))


def manhatten(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def part1(dist):
    cnt = 0
    for (a,da),(b,db) in itertools.combinations(dist.items(), 2):
        d = manhatten(a,b)
        if d == 2:
            if db-da-d >= 100:
                cnt += 1
    return cnt


def part2(dist):
    cnt = 0
    for (a,da),(b,db) in itertools.combinations(dist.items(), 2):
        d = manhatten(a,b)
        if d <= 20:
            if db-da-d >= 100:
                cnt += 1
    return cnt
