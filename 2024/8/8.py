import itertools
DEBUG = False

def calculate_antinodes(c1, c2):
    """Given two tuples of (x, y) return the two tuples that would be antinodes"""
    dx = c2[0] - c1[0]
    dy = c2[1] - c1[1]
    return ((c1[0] - dx, c1[1] - dy), 
            (c2[0] + dx, c2[1] + dy))
    
def calculate_resonant_anti_nodes(c1, c2, w, h):
    """ This may contain some values off the grid, but it will stop after the first off
    """
    dx = c2[0] - c1[0]
    dy = c2[1] - c1[1]
    antinodes = []
    # extend from c1 to the "right" until we're off the grid
    p = (c1[0] - dx, c1[1] - dy)
    while p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h:
        antinodes.append(p)
        p = (p[0] - dx, p[1] - dy)
    # extend from c1 to the "left" until we're off the grid
    p = (c1[0] + dx, c1[1] + dy)
    while p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h:
        antinodes.append(p)
        p = (p[0] + dx, p[1] + dy)

    # extend from c2 to the "right" until we're off the grid
    p = (c2[0] - dx, c2[1] - dy)
    while p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h:
        antinodes.append(p)
        p = (p[0] - dx, p[1] - dy)
    # extend from c2 to the "left" until we're off the grid
    p = (c2[0] + dx, c2[1] + dy)
    while p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h:
        antinodes.append(p)
        p = (p[0] + dx, p[1] + dy)

    return antinodes

    
def get_nodes(s):
    d = {}
    for y, l in enumerate(s.split()):
        for x, c in enumerate(list(l)):
            if c.isupper() or c.islower() or c.isdigit():
                d.setdefault(c, []).append((x, y))
    return d

def get_all_antinodes(nodes_dict, w, h, resonance=False):
    antinodes = []
    for k in nodes_dict.keys():
        nodes_list = nodes_dict[k]
        for pair in itertools.combinations(nodes_list, r=2):
            if resonance:
                candidate_antinodes = calculate_resonant_anti_nodes(pair[0], pair[1], w, h)
            else:
                candidate_antinodes = calculate_antinodes(pair[0], pair[1])
            for c in candidate_antinodes:
                if c[0] >= 0 and c[0] < w and c[1] >= 0 and c[1] < h:
                    antinodes.append(c)
    return set(antinodes)

with open('input.txt', 'r') as f:
    s = f.read()

rows = s.split()
w, h = len(rows[0]), len(rows)
nodes = get_nodes(s)
antinodes = get_all_antinodes(nodes, w, h)
res_antinodes = get_all_antinodes(nodes, w, h, resonance=True)
print(len(antinodes))
print(len(res_antinodes))

if DEBUG:
    array = []
    for r in rows:
        array.append(list(r))

    for a in res_antinodes:
        c = array[a[1]][a[0]]
        if not (c.isupper() or c.islower() or c.isdigit()):
            array[a[1]][a[0]] = '#'
        
    for row in array:
        print(''.join(row))