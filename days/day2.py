def parse(inp):
    return [[int(n) for n in line.split()] for line in inp.splitlines()]


def check(report):
    if report[0] > report[1]:
        report = list(reversed(report))
    for a,b in zip(report, report[1:]):
        if a > b:
            return False
        if not (1 <= b-a <= 3):
            return False
    return True


def part1(reports):
    return sum(check(report) for report in reports)


def part2(reports):
    cnt = 0
    for report in reports:
        if check(report):
            cnt += 1
            continue
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if check(new_report):
                cnt += 1
                break
    return cnt
