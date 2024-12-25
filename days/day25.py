def part1(inp):
    chunks = inp.split('\n\n')
    keys = []
    locks = []

    W, H = 5, 5

    for chunk in chunks:
        rows = chunk.splitlines()
        if all(c == '#' for c in rows[0]):
            lock = [0] * W
            for row in rows[1:]:
                for i, c in enumerate(row):
                    lock[i] += c == '#'
            locks.append(lock)
        else:
            key = [0] * W
            for row in rows[:-1]:
                for i, c in enumerate(row):
                    key[i] += c == '#'
            keys.append(key)

    cnt = 0
    for key in keys:
        for lock in locks:
            check = any(k+l > H for k,l in zip(key, lock))
            cnt += not(check)
    return cnt
