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


def run_path(w, h, start, obstacles):
    x,y = start
    dx, dy = 0,-1
    visited = set()
    while 0 <= x < w and 0 <= y < h:
        nx, ny = x+dx, y+dy
        if (nx,ny) in obstacles:
            dx, dy = turn_right(dx, dy)
        else:
            visited.add((x,y))
            x, y = nx, ny
    return visited


def part1(inp):
    return len(run_path(*inp))


def part2(inp):
    w, h, start, obstacles = inp
    cnt = 0
    visited = run_path(*inp)

    for n_obstacle in visited:
        if n_obstacle == start:
            continue

        x,y = start
        dx, dy = 0,-1
        visited2 = set()
        while 0 <= x < w and 0 <= y < h:
            nx, ny = x+dx, y+dy
            if (x,y,dx,dy) in visited2:
                cnt += 1
                break
            elif (nx,ny) in obstacles or (nx,ny) == n_obstacle:
                dx, dy = turn_right(dx, dy)
            else:
                visited2.add((x,y,dx,dy))
                x, y = nx, ny
    return cnt
