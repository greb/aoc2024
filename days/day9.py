import itertools
import collections


def part1(inp):
    segments = [int(n) for n in inp.strip()]

    disk = []
    for segment_id, segment_n in enumerate(segments):
        if segment_id & 1:
            for _ in range(segment_n):
                disk.append(None)
        else:
            file_id = segment_id // 2
            for _ in range(segment_n):
                disk.append(file_id)

    checksum = 0
    for block in itertools.count():
        if block == len(disk):
            break

        if disk[block] is None:
            last_file = disk.pop()
            while last_file is None:
                last_file = disk.pop()
            disk[block] = last_file

        checksum += block*disk[block]
    return checksum


def part2(inp):
    free = []
    files = []
    offset = 0
    for i, n in enumerate(int(n) for n in inp.strip()):
        if i & 1:
            free.append((n, offset))
        else:
            files.append((n, offset))
        offset += n

    checksum = 0

    for fid, (n, offset) in reversed(list(enumerate(files))):
        found_free = False
        for idx, (free_n, free_offset) in enumerate(free):
            if free_offset > offset:
                break
            if free_n >= n:
                found_free = True
                break

        if found_free:
            for i in range(n):
                checksum += (free_offset+i) * fid
            if free_n > n:
                free[idx] = free_n-n, free_offset+n
            else:
                free.pop(idx)
        else:
            for i in range(n):
                checksum += (offset+i) * fid

    return checksum
