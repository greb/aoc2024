import heapq

def parse(inp):
    rows = inp.splitlines()
    w, h = len(rows[0]), len(rows)

    walls = set()
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            match c:
                case 'S':
                    start = (x,y)
                case 'E':
                    end = (x,y)
                case '#':
                    walls.add((x,y))
    return dijkstra((start, end, walls))

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

def dijkstra(inp):
    start, end, walls = inp
    visited = set()
    stack = [(0, 0, [start], start)]
    best = None
    touched = set()

    while stack:
        score, dir, path, curr = heapq.heappop(stack)
        if curr == end:
            if best and score > best:
                break
            best = score
            touched |= set(path)
        visited.add((dir, curr))

        moved = tuple(c+d for c,d in zip(curr, DIRS[dir]))
        if moved not in walls and (dir, moved) not in visited:
            heapq.heappush(stack, (score+1, dir, path+[moved], moved))

        cw, ccw = (dir+1)%4, (dir-1)%4
        if (cw, curr) not in visited:
            heapq.heappush(stack, (score+1000, cw, path, curr))
        if (ccw, curr) not in visited:
            heapq.heappush(stack, (score+1000, ccw, path, curr))

    return best, len(touched)


def part1(inp):
    return inp[0]


def part2(inp):
    return inp[1]
