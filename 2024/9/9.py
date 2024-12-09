def disk_map_to_blocks(disk):
    d_map = ''
    id = 0
    m = 1
    for i, c in enumerate(disk):
        if m == 1:
            d_map += str(id) * int(c)
            id += 1
        else:
            d_map += '.' * int(c)
        m *= -1
    return d_map

def get_last_disc_block(disc_block):
    for i, c in enumerate(disc_block[::-1]):
        if c.isnumeric():
            return len(disc_block) - i
        
s = '009..111...2...333.44.5555.6666.777.88889.'
print(get_last_disc_block(s))
            
def is_valid(disc_block):
    m = 'num'
    switched_count = 0
    for n in disc_block:
        if n.isnumeric():
            if switched_count == 0:
                continue
            else:
                return False
        else:
            switched_count += 1
    return True

def compact_disk_map(d_map):
    d_block = disk_map_to_blocks(d_map)
    i = 0
    while not is_valid(d_block):
        last_n_index = get_last_disc_block(d_block)
        first_dot_index = d_block.index('.')
        l = list(d_block)
        l[first_dot_index] = l[last_n_index-1]
        l[last_n_index-1] = '.'
        d_block = ''.join(l)
        i += 1
    return d_block

def get_checksum(d_block):
    s = 0
    for i, c in enumerate(d_block):
        if c.isnumeric():
            s += i * int(c)
        else:
            break
    return s


m = compact_disk_map('2333133121414131402')
s = get_checksum(m)
print(s)