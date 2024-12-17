import re

def parse(inp):
    regs, code = inp.split('\n\n')
    regs = [int(re.search(r'\d+', r).group()) for r in regs.splitlines()]
    code = [int(n) for n in code.split(' ')[1].split(',')]
    return regs, code


def run(regs, code):
    ip = 0
    out = []

    def decode_combo(val):
        if val <= 3:
            return val
        elif val == 7:
            raise Exception('Invalid combo operand')
        return regs[val & 0b11]

    while ip < len(code):
        opcode = code[ip]
        operand = code[ip+1]
        combo = decode_combo(operand)

        nxt_ip = ip + 2
        match opcode:
            case 0:
                regs[0] = regs[0] // (2**combo)
            case 1:
                regs[1] = regs[1] ^ operand
            case 2:
                regs[1] = combo % 8
            case 3:
                if regs[0] != 0:
                    nxt_ip = operand
            case 4:
                regs[1] = regs[1] ^ regs[2]
            case 5:
                val = combo % 8
                out.append(val)
            case 6:
                regs[1] = regs[0] // (2**combo)
            case 7:
                regs[2] = regs[0] // (2**combo)
        ip = nxt_ip
    return out


def part1(inp):
    out = run(*inp)
    return ','.join(map(str, out))


def part2(inp):
    _, code = inp
    found = []

    stack = [(0, code)]
    while stack:
        a, check = stack.pop()
        *head, last = check

        for i in range(8):
            nxt = a+i
            out = run([nxt, 0, 0], code)
            if out[0] == last:
                if not head:
                    found.append(nxt)
                else:
                    stack.append((nxt*8, head))

    return min(found)
