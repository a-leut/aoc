def disk_map_to_blocks(disk):
    d_map = []
    id = 0
    m = 1
    for i, c in enumerate(disk):
        if m == 1:
            d_map.append(str(id) * int(c))
            id += 1
        else:
            d_map.append('.' * int(c))
        m *= -1
    return ''.join(d_map)
            
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
    i = 0
    j = len(d_map) - 1
    final = ''
    while i != j + 1:
        if d_map[i].isnumeric():
            final += d_map[i]
            i += 1
        elif d_map[j].isnumeric():
            final += d_map[j]
            j -= 1
            i += 1
        else:
            j -= 1
    return final

def get_checksum(d_block):
    s = 0
    for i, c in enumerate(d_block):
        if c.isnumeric():
            s += i * int(c)
        else:
            continue
    return s

with open('input.txt', 'r') as f:
    s = f.read()
# s = '2333133121414131402'
d_block = disk_map_to_blocks(s)
with open('dblock.txt', 'w') as f:
    f.write(d_block)
m = compact_disk_map(d_block)
with open('compact.txt', 'w') as f:
    f.write(m)
print(m)
s = get_checksum(m)
print(s)