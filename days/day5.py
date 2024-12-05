def parse(inp):
    rules, updates = inp.split('\n\n')
    after = dict()
    for rule in rules.splitlines():
        a, b = rule.split('|')
        after.setdefault(int(b), set()).add(int(a))

    def reorder(update):
        # Dirty little topological sort
        def index(page):
            return len(after.get(page, set()).intersection(update))
        return sorted(update, key=index)

    updates = [[int(p) for p in line.split(',')] for line in
               updates.splitlines()]
    return reorder, updates


def part1(inp):
    score = 0
    reorder, updates = inp
    for update in updates:
        reordered = reorder(update)
        if update == reordered:
            score += update[len(update)//2]
    return score


def part2(inp):
    score = 0
    reorder, updates = inp
    for update in updates:
        reordered = reorder(update)
        if update != reordered:
            score += reordered[len(reordered)//2]
    return score


