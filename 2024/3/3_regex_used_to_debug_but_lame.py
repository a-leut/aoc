# i used this to debug my cool version

import re

DIGITS = [str(x) for x in range(10)]

def get_muls(s):
    # modes: nuttin, start_mul, first_num, second_num
    total = 0
    pairs = []
    mode = 'nuttin'
    enabled_mode = 'do'
    n1 = ''
    n2 = ''
    for i in range(len(s)):
        if s[i] == '(' and i > 3 and s[i-3:i] == 'mul':
            mode = 'start_num'
        elif mode == 'start_num':
            if s[i] in DIGITS:
                n1 += s[i]
                if len(n1) > 3:
                    mode = 'nuttin'
                    n1 = ''
            elif s[i] == ',' and len(n1) > 0:
                mode = 'second_num'
            else:
                mode = 'nuttin'
        elif mode == 'second_num':
            if s[i] in DIGITS:
                n2 += s[i]
                if len(n2) > 3:
                    mode = 'nuttin'
                    n1 = ''
                    n2 = ''
            elif s[i] == ')' and len(n2) > 0:
                print('found 1')
                print(n1, n2)
                total += int(n1) * int(n2)
                pairs.append((int(n1), int(n2)))
                mode = 'nuttin'
                n1 = ''
                n2 = ''
            else:
                mode = 'nuttin'
                n1 = ''
                n2 = ''
    return pairs

def compute_valid_mul_sum(corrupted_memory):
    pairs = []
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, corrupted_memory)
    return [(int(x), int(y)) for x, y in matches]

def find_missing_pairs(l1, l2):
    """
    Find the pairs in l2 that are missing from l1.
    
    Args:
    - l1 (list of tuples): The first list of tuples.
    - l2 (list of tuples): The second list of tuples to compare against l1.

    Returns:
    - list of tuples: The pairs in l2 that are not in l1.
    """
    # Convert l1 to a set for faster lookup
    set_l1 = set(l1)
    
    # Use list comprehension to find tuples in l2 but not in l1
    missing_pairs = [pair for pair in l2 if pair not in set_l1]
    
    return missing_pairs



with open('input.txt', 'r') as f:
    mem = f.read()
    
# Compute the sum of valid `mul(X,Y)` instructions
pairs_1 = get_muls(mem)
pairs_2 = compute_valid_mul_sum(mem)

with open('p1', 'w') as f:
    for p in pairs_1:
        f.write(f'{p[0]}, {p[1]}\n')
        
with open('p2', 'w') as f:
    for p in pairs_2:
        f.write(f'{p[0]}, {p[1]}\n')


missing = find_missing_pairs(pairs_1, pairs_2)
print(missing)
