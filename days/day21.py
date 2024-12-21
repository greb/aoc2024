import functools
import itertools

def parse(inp):
    return inp.splitlines()

def construct_lut(keys):
    return {key: (x,y) for y,row in enumerate(keys)
            for x,key in enumerate(row)
            if key != ' '}

DIRS = {'>':(1,0), 'v':(0,1), '<':(-1,0), '^':(0,-1)}

# door has strange numpad layout. It's 123, not 321. Took a while to find
DOOR = ['789', '456', '123', ' 0A']
DOOR_LUT = construct_lut(DOOR)

PANEL = [' ^A', '<v>']
PANEL_LUT = construct_lut(PANEL)


def check_perm(pos, perm, lookup):
    x, y = pos
    for button in perm:
        dx, dy = DIRS[button]
        x, y = x+dx, y+dy
        if (x,y) not in lookup.values():
            return False
    return True


def button_perms(pos, nxt, lookup):
    x, y = pos
    nx, ny = nxt
    dx, dy = nx-x, ny-y

    buttons = ''
    if dx >= 0:
        buttons += '>' * dx
    else:
        buttons += '<' * abs(dx)
    if dy >= 0:
        buttons += 'v' * dy
    else:
        buttons += '^' * abs(dy)

    return set(itertools.permutations(buttons))


@functools.cache
def min_path(sequence, depth, is_door=True, pos=None):
    lookup = DOOR_LUT if is_door else PANEL_LUT
    if not sequence:
        return 0
    if not pos:
        pos = lookup['A']
    nxt = lookup[sequence[0]]

    lens = []
    for perm in button_perms(pos, nxt, lookup):
        if not check_perm(pos, perm, lookup):
            continue
        path = ''.join(perm) + 'A'
        if depth:
            lens.append(min_path(path, depth-1, is_door=False))
        else:
            lens.append(len(path))
    min_len = min(lens)
    return min_len + min_path(sequence[1:], depth, is_door, nxt)


def part1(codes):
    cnt = 0
    for code in codes:
        num = int(code[:-1])
        cnt += num * min_path(code, 2)
    return cnt


def part2(codes):
    cnt = 0
    for code in codes:
        num = int(code[:-1])
        cnt += num * min_path(code, 25)
    return cnt

