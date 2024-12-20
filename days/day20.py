import collections

def parse(inp):
    walls = set()

    for y, row in enumerate(inp.splitlines()):
        for x,c in enumerate(row):
            match c:
                case 'S':
                    start = x,y
                case 'E':
                    end = x,y
                case '#':
                    walls.add((x,y))
    return walls, start, end

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
def neighbors(pos):
    for dir in DIRS:
        yield tuple(p+d for p,d in zip(pos, dir))

def part1(inp):
    walls, start, end = inp

    shortest = dict()
    queue = collections.deque([(0,start)])
    while queue:
        cnt, curr = queue.popleft()
        for nxt in neighbors(curr):
            if nxt in shortest:
                continue
            shortest[nxt] = cnt+1, curr
            if nxt not in walls:
                queue.append((cnt+1, nxt))


    counter = collections.Counter()
    for curr, (cnt, prev) in shortest.items():
        if curr not in walls:
            continue
        for nxt in neighbors(curr):
            if nxt == prev or nxt in walls or nxt not in shortest:
                continue
            cheat_cnt = shortest[nxt][0] - cnt - 1
            counter[cheat_cnt] += 1

    return sum(n for c,n in counter.items() if c >= 100)

