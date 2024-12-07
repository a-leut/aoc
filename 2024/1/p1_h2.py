loc_ids_1 = []
loc_ids_2 = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        l1, l2 = line.split()
        loc_ids_1.append(int(l1))
        loc_ids_2.append(int(l2))

target_ids = set(loc_ids_1)
counter = {i: 0 for i in target_ids}  # not use the collections.Counter because we're cool

for n in loc_ids_2:
    if n in counter.keys():
        counter[n] += 1

sim_score = 0
for n in loc_ids_1:
    sim_score += n * counter[n]

print(sim_score)