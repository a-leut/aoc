from tqdm import tqdm

def get_ordering_and_updates(s):
    s1, s2 = s.split('\n\n')
    p = [l.split('|') for l in s1.split()]
    u = [l.split(',') for l in s2.split()]
    return p, u

def is_valid_update(u, pairs):
    # first make a dict of number to rank so we dont degenerate to O^2
    rank = {l[0]: l[1] for l in zip(u, range(len(u)))}
    for p in pairs:
        if p[0] in u and p[1] in u and rank[p[0]] > rank[p[1]]:
            return False
    return True

def get_middle_sum_valid(pairs, updates):
    total = 0
    for u in updates:
        # we hope the list has odd number of elements
        if is_valid_update(u, pairs):
            total += int(u[len(u)//2])
    return total

def reorder_update(u, pairs):
    # we assume all can be reordered
    #pairs_that_order = [p for p in pairs if p[0] in u and p[1] in u]
    ordered_values = []
    for p in pairs:
        print(p)
        if len(ordered_values) == len(u):
            break
        if len(ordered_values) == 0:
            ordered_values = p
        else:
            if (p[0] in ordered_values and p[1] in ordered_values) \
            or (p[0] not in ordered_values and p[1] not in ordered_values):
                print('skip')
                continue
            elif p[0] in ordered_values and p[1] not in ordered_values:
                print('found p0')
                i = ordered_values.index(p[0])
                ordered_values.insert(i + 1, p[1])
            elif p[1] in ordered_values and p[0] not in ordered_values:
                print('found p1')
                i = ordered_values.index(p[1])
                ordered_values.insert(i, p[0])
            print(ordered_values)
    return ordered_values

            

def get_middle_sum_invalid_reorder(pairs, updates):
    total = 0
    for u in updates:
        # we hope the list has odd number of elements
        if not is_valid_update(u, pairs):
            nu = reorder_update(u, pairs)
            print(nu)
            total += int(nu[len(nu)//2])
    return total

with open('input.txt', 'r') as f:
    s = f.read()

# pairs, updates = get_ordering_and_updates(s)
# s = get_middle_sum_valid(pairs, updates)
# print(s)

s = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,97,47,61,53
'''

pairs, updates = get_ordering_and_updates(s)
n = get_middle_sum_invalid_reorder(pairs, updates)
print(n)