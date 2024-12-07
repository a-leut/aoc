import itertools
from tqdm import tqdm

memonized_signs = {}

def s_to_p(s):
    p = []
    for l in s.splitlines():
        t, vals = l.split(': ')
        t = int(t)
        vals = [int(n) for n in vals.split(' ')]
        p.append((t, vals))
    return p


def evaluate_function(values, signs):
    last_val = values[0]
    for i, sign in enumerate(signs):
        if sign == '*':
            last_val = last_val * values[i + 1]
        elif sign == '+':
            last_val = last_val + values[i + 1]
        else:
            last_val = int(str(last_val) + str(values[i + 1]))
    return last_val

def is_valid_formula(target, values, operations=['+', '*']):

    signs = list(itertools.product(operations, repeat=len(values) - 1))

    for s in signs:
        e = evaluate_function(values, s)
        if target == e:
            return True
    return False
        

def get_p1(p):
    s = 0
    for t, values in p:
        if is_valid_formula(t, values):
            s += t
    return s

def get_p2(p):
    s = 0
    for t, values in tqdm(p):
        if is_valid_formula(t, values, operations=['+', '*', '||']):
            s += t
    return s

with open('input.txt', 'r') as f:
    s = f.read()
p = s_to_p(s)
p1 = get_p1(p)
print(p1)

p2 = get_p2(p)
print(p2)