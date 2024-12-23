import collections
import itertools

def parse(inp):
    verts = set()
    edges = collections.defaultdict(set)
    for line in inp.splitlines():
        a, b = line.split('-')
        verts.add(a)
        verts.add(b)
        edges[a].add(b)
        edges[b].add(a)
    return verts, edges


def part1(inp):
    verts, edges = inp
    triangles = set()
    for v in verts:
        if v[0] != 't':
            continue
        for a,b in itertools.combinations(edges[v], 2):
            if a in edges[b]:
                triangles.add(frozenset((v, a, b)))
    return len(triangles)


def part2(inp):
    verts, edges = inp

    # Using the Bron-Kerbosch algo. Thanks wikipedia!
    stack = [(verts, set(), set())]
    cliques = []
    while stack:
        verts, clique, exclude = stack.pop()
        if not verts and not exclude:
            cliques.append(clique)

        for vert in verts:
            n_verts = (verts & edges[vert]) - exclude
            n_clique = clique | {vert}
            n_exclude = exclude & edges[vert]
            stack.append((n_verts, n_clique, n_exclude))
            exclude |= {vert}

    best = max(cliques, key=len)
    return ','.join(sorted(best))
