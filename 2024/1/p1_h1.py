loc_ids_1 = []
loc_ids_2 = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        l1, l2 = line.split()
        loc_ids_1.append(int(l1))
        loc_ids_2.append(int(l2))

loc_ids_1.sort()
loc_ids_2.sort()

d = 0
for t in zip(loc_ids_1, loc_ids_2):
    d += abs(t[0] - t[1])

print(d)