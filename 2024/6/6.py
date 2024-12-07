def get_next_grid(grid, player_pos):
    """ Returns a new grid and starting pos after running a step, None if invalid state
    """
    h = len(grid)
    w = len(grid[0])
    px, py = player_pos
    c = grid[py][px]
    # check if we're in an end state
    if c == '^' and py == 0 \
    or c == 'v' and py == h - 1 \
    or c == '>' and px == w - 1 \
    or c == '<' and px == 0:
        return None, None
    # get our candidate target square, t
    t = None
    if c == '^':
        t = grid[py-1][px]
        if t == '#':
            grid[py][px] = '>'
        else:
            grid[py-1][px] = '^'
            grid[py][px] = '.'
            player_pos = (px, py - 1)
    elif c == 'v':
        t = grid[py+1][px]
        if t == '#':
            grid[py][px] = '<'
        else:
            grid[py+1][px] = 'v'
            grid[py][px] = '.'
            player_pos = (px, py + 1)
    elif c == '>':
        t = grid[py][px+1]
        if t == '#':
            grid[py][px] = 'v'
        else:
            grid[py][px+1] = '>'
            grid[py][px] = '.'
            player_pos = (px + 1, py)
    elif c == '<':
        t = grid[py][px-1]
        if t == '#':
            grid[py][px] = '^'
        else:
            grid[py][px-1] = '<'
            grid[py][px] = '.'
            player_pos = (px - 1, py)
    return grid, player_pos

def s_to_grid(s):
    g = []
    starting_pos = None
    y = 0
    for r in s.split():
        for c in ['^', '>', '<', 'v']:
            if c in r:
                starting_pos = (r.index(c), y)
        g.append(list(r))
        y += 1
    return g, starting_pos

with open('input.txt', 'r') as f:
    s = f.read()
    
g, starting_pos = s_to_grid(s)
visited = [starting_pos]
next_grid, next_pos = get_next_grid(g, starting_pos)
while next_grid:
    visited.append(next_pos)
    next_grid, next_pos = get_next_grid(next_grid, next_pos)
print(len(set(visited)))
