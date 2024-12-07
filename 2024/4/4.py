from typing import List

T = 'XMAS' # target word
L = len(T) # minimal speed up
V = [      # vectors to consider for direction
    {'name': 'left', 'x': -1, 'y': 0},
    {'name': 'right', 'x': 1, 'y': 0},
    {'name': 'up', 'x': 0, 'y': -1},
    {'name': 'down', 'x': 0, 'y': 1},
    {'name': 'up-left', 'x': -1, 'y': -1},
    {'name': 'up-right', 'x': 1, 'y': -1},
    {'name': 'down-left', 'x': -1, 'y': 1},
    {'name': 'down-right', 'x': 1, 'y': 1},
]

def string_to_letter_grid(input: str) -> List[List[str]]:
    return [list(l) for l in input.split()]

def count_xmas(g: List[List[str]]) -> int:
    if len(g) == 0:
        return 0
    w = len(g[0])
    h = len(g)
    c = 0
    for x in range(w):
        for y in range(h):
            if g[y][x] == T[0]:
                for v in V:  
                    dest_x = x + (v['x'] * (len(T) - 1))
                    dest_y = y + (v['y'] * (len(T) - 1))
                    if dest_x < 0 or dest_x > w - 1 or dest_y < 0 or dest_y > h - 1:
                        continue
                    # check if we match
                    candiate_match = ''.join([g[y + (v['y'] * i)][x + (v['x'] * i)] for i in range(1, len(T))])
                    if candiate_match == T[1:]:
                        c += 1
    return c

def count_x_mas(g: List[List[str]]) -> int:
    if len(g) == 0:
        return 0
    w = len(g[0])
    h = len(g)
    c = 0
    for x in range(w):
        for y in range(h):
            if g[y][x] == 'A':
                if x < 1 or y > w - 2 or y < 1 or y > h - 2:
                    continue
                try:
                    if ((g[y - 1][x - 1] == 'M' and g[y + 1][x + 1] == 'S') \
                    # down right
                    or (g[y - 1][x - 1] == 'S' and g[y + 1][x + 1] == 'M')) \
                    and ((g[y - 1][x + 1] == 'M' and g[y + 1][x - 1] == 'S') \
                    # bottom left
                    or (g[y - 1][x + 1] == 'S' and g[y + 1][x - 1] == 'M')):
                        c += 1 
                except:
                    pass
    return c


with open('input.txt', 'r') as f:
    g = string_to_letter_grid(f.read())

c1 = count_xmas(g)
print(c1)

c2 = count_x_mas(g)
print(c2)

