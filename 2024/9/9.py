def disk_map_to_blocks(disk):
    d_map = []
    id = 0
    m = 1
    for c in disk:
        if m == 1:
            d_map.extend([id] * int(c))
            id += 1
        else:
            d_map.extend(['.'] * int(c))
        m *= -1
    return d_map
            
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
    print(d_map)
    i = 0
    j = len(d_map) - 1
    final = []
    while i != j + 1:
        if str(d_map[i]).isnumeric():
            final.append(d_map[i])
            i += 1
        elif str(d_map[j]).isnumeric():
            final.append(d_map[j])
            j -= 1
            i += 1
        else:
            j -= 1
    return final

def get_checksum(d_block):
    s = 0
    for i, c in enumerate(d_block):
        if str(c).isnumeric():
            s += i * int(c)
        else:
            continue
    return s

with open('input.txt', 'r') as f:
    s = f.read()
# s = '233313312141413140211'
d_block = disk_map_to_blocks(s)
with open('dblock.txt', 'w') as f:
    f.write(str(d_block))
m = compact_disk_map(d_block)
with open('compact.txt', 'w') as f:
    f.write(str(m))
s = get_checksum(m)
print(s)