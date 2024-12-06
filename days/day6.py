import itertools

def parse(inp):
    rows = inp.splitlines()
    w, h = len(rows[0]), len(rows)
    obstacles = set()
    for y, row in enumerate(rows):
        for x, tile in enumerate(row):
            match tile:
                case '#':
                    obstacles.add((x,y))
                case '^':
                    start = (x,y)
    return w, h, start,obstacles


def turn_right(dx, dy):
    return -dy,dx


def part1(inp):
    w, h, start, obstacles = inp
    visited = set()

    x,y = start
    dx, dy = 0,-1
    while 0 <= x < w and 0 <= y < h:
        nx, ny = x+dx, y+dy
        if (nx,ny) in obstacles:
            dx, dy = turn_right(dx, dy)
        else:
            visited.add((x,y))
            x, y = nx, ny
    return len(visited)


def part2(inp):
    w, h, start, obstacles = inp
    cnt = 0

    for ox,oy in itertools.product(range(w),range(h)):
        if (ox,oy) in obstacles or (ox,oy) == start:
            continue
        visited = set()
        n_obstacles = obstacles.copy()
        n_obstacles.add((ox,oy))

        x,y = start
        dx, dy = 0,-1
        while 0 <= x < w and 0 <= y < h:
            nx, ny = x+dx, y+dy
            if (x,y,dx,dy) in visited:
                cnt += 1
                break
            elif (nx,ny) in n_obstacles:
                dx, dy = turn_right(dx, dy)
            else:
                visited.add((x,y,dx,dy))
                x, y = nx, ny
    return cnt
