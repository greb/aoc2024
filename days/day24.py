import re
import collections

def parse(inp):
    signal_lines, wires_lines = inp.split('\n\n')

    signals = dict()
    for s in signal_lines.splitlines():
        n, v = re.match(r'(.*): (\d)', s).groups()
        signals[n] = bool(int(v))

    wires = dict()
    for w in wires_lines.splitlines():
        *conf, out = re.match(r'(\w*) (\w*) (\w*) -> (\w*)', w).groups()
        wires[out] = conf

    return signals, wires


def part1(inp):
    signals, wires = inp
    stack = list(wires.keys())
    while stack:
        out = stack.pop()
        if out in signals:
            continue

        a, op, b = wires[out]
        if a in signals and b in signals:
            match op:
                case 'AND':
                    signals[out] = signals[a] and signals[b]
                case 'OR':
                    signals[out] = signals[a] or signals[b]
                case 'XOR':
                    signals[out] = signals[a] != signals[b]
        else:
            stack.append(out)
            if a not in signals:
                stack.append(a)
            if b not in signals:
                stack.append(b)

    num = 0
    zs = sorted(n for n in signals.keys() if n[0] == 'z')
    for digit in reversed(zs):
        num *= 2
        num += signals[digit]
    return num


def part2(inp):
    _, wires = inp

    last_z = max(o for o in wires.keys() if o[0] == 'z')

    # Assuming a simple ripple carrier adder
    swapped = set()
    for out, (a, op, b) in wires.items():
        # Output bits must come from XOR except the last one
        if out[0] == 'z' and op != 'XOR' and out != last_z:
            swapped.add(out)

        if op == 'AND':
            # ANDs can only feed into ORs, except bit 0
            if 'x00' in [a,b]:
                continue
            for a2, op2, b2 in wires.values():
                if op2 != 'OR' and (out == a2 or out == b2):
                    swapped.add(out)
        elif op == 'OR':
            # ORs must not feed into ORs
            for a2, op2, b2 in wires.values():
                if op2 == 'OR' and (out == a2 or out == b2):
                    swapped.add(out)

        elif op == 'XOR':
            # XOR must either be an output bit or only have x or y input bits
            if out[0] != 'z' and a[0] not in 'xy' and b[0] not in 'xy':
                swapped.add(out)

            # XORs must not feed into ORs
            for a2, op2, b2 in wires.values():
                if op2 == 'OR' and (out == a2 or out == b2):
                    swapped.add(out)


    return ','.join(sorted(swapped))

