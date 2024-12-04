import collections
import itertools

Grid = collections.namedtuple('Grid', ['w', 'h', 'arr'])
dirs = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1, -1)]

def parse(inp):
    arr = [[c for c in line] for line in inp.splitlines()]
    w,h = len(arr[0]), len(arr)
    return Grid(w, h, arr)


def part1(grid):
    cnt = 0
    for x,y in itertools.product(range(grid.w), range(grid.h)):
        for dx,dy in dirs:
            seg = [grid.arr[y][x]]
            nx, ny = x, y
            for _ in range(3):
                nx, ny = nx+dx, ny+dy
                if 0 <= nx < grid.w and 0 <= ny < grid.h:
                    seg.append(grid.arr[ny][nx])
            if ''.join(seg) == 'XMAS':
                cnt += 1
    return cnt


def part2(grid):
    cnt = 0
    valid = [('M', 'S'), ('S', 'M')]
    for x,y in itertools.product(range(1, grid.w-1),range(1, grid.h-1)):
        if grid.arr[y][x] != 'A':
            continue
        seg_a = grid.arr[y-1][x-1], grid.arr[y+1][x+1]
        seg_b = grid.arr[y-1][x+1], grid.arr[y+1][x-1]
        if seg_a in valid and seg_b in valid:
            cnt += 1
    return cnt
