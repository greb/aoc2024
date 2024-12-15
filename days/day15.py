DIRS = {'>': (1,0), 'v': (0,1), '<': (-1,0), '^': (0,-1)}


def parse(inp):
    maze_lines, move_lines = inp.split('\n\n')

    robot = None
    maze = dict()
    maze_lines = maze_lines.splitlines()
    w, h = len(maze_lines[0]), len(maze_lines)
    for y, row in enumerate(maze_lines):
        for x, c in enumerate(row):
            pos = x, y
            if c == '@':
                robot = pos
                maze[pos] = '.'
            else:
                maze[pos] = c

    moves = [DIRS[c] for c in move_lines if c in DIRS]
    return robot, maze, moves, w, h


def debug_maze(robot, maze, w, h):
    for y in range(h):
        line = []
        for x in range(w):
            if (x,y) == robot:
                line.append('@')
            else:
                line.append(maze[(x,y)])
        print(''.join(line))


def can_move1(pos, maze, move):
    nxt = tuple(a+b for a,b in zip(pos, move))
    if maze[nxt] == '#':
        return False

    if maze[nxt] == 'O' and not can_move1(nxt, maze, move):
        return False

    maze[pos], maze[nxt] = maze[nxt], maze[pos]
    return nxt


def part1(inp):
    robot, maze, moves, w, h = inp
    maze = maze.copy()

    for move in moves:
        copy = maze.copy()
        nxt = can_move1(robot, maze, move)
        if nxt:
            robot = nxt
        else:
            maze = copy
    score = 0
    for (x,y), c in maze.items():
        if c == 'O':
            score += x+ 100*y
    return score


def can_move2(pos, maze, move):
    nxt = x,y = tuple(a+b for a,b in zip(pos, move))
    if maze[nxt] == '#':
        return False

    if maze[nxt] == '[':
        check = (can_move2((x+1,y), maze, move) and
                can_move2((x,y), maze, move))
        if not check:
            return False
    if maze[nxt] == ']':
        check = (can_move2((x-1,y), maze, move) and
                 can_move2((x,y), maze, move))
        if not check:
            return False

    maze[pos], maze[nxt] = maze[nxt], maze[pos]
    return nxt


def part2(inp):
    robot, maze, moves, w, h = inp

    robot = robot[0]*2, robot[1]
    new_maze = dict()
    for (x,y), c in maze.items():
        if c == 'O':
            new_maze[(x*2, y)] = '['
            new_maze[(x*2+1, y)] = ']'
        else:
            new_maze[(x*2, y)] = c
            new_maze[(x*2+1, y)] = c
    maze = new_maze

    for move in moves:
        copy = maze.copy()
        nxt = can_move2(robot, maze, move)
        if nxt:
            robot = nxt
        else:
            maze = copy
    score = 0
    for (x,y), c in maze.items():
        if c == '[':
            score += x+ 100*y
    return score
