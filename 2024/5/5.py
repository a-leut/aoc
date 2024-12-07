from tqdm import tqdm
from collections import defaultdict, deque

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

def kahns_algorithm(graph_dict):
    # get list of nodes
    all_nodes = set(graph_dict.keys())
    for nbrs in graph_dict.values():
        all_nodes.update(nbrs)
    # compute degree
    in_degree = {node: 0 for node in all_nodes}
    for node, neighbors in graph_dict.items():
        for nbr in neighbors:
            in_degree[nbr] = in_degree.get(nbr, 0) + 1
    # sort with khans algo
    queue = [node for node in all_nodes if in_degree[node] == 0]
    topo_order = []
    while queue:
        current = queue.pop()
        topo_order.append(current)
        for nxt in graph_dict.get(current, []):
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)
    return topo_order

def reorder_update(u, topo_order):
    reordered = []
    for i in topo_order:
        if i in u:
            reordered.append(i)
    return reordered            

def get_middle_sum_invalid_reorder(pairs, updates):
    total = 0
    for u in updates:
        if not is_valid_update(u, pairs):
            g = {}
            for p in pairs:
                if p[0] in u and p[1] in u:
                    if p[0] in g:
                        g[p[0]].append(p[1])
                    else:
                        g[p[0]] = [p[1]]
            for node in u:
                if node not in g:
                    g[node] = []
            topo_order = kahns_algorithm(g)
            nu = reorder_update(u, topo_order)
            total += int(nu[len(nu)//2])
    return total

with open('input.txt', 'r') as f:
    s = f.read()
pairs, updates = get_ordering_and_updates(s)
print(get_middle_sum_valid(pairs, updates))
print(get_middle_sum_invalid_reorder(pairs, updates))
