def is_unsafe_pair(n, p, direction):
    delta = n - p
    return delta > 0 and direction == 'asc' or delta < 0 and direction == 'desc' \
            or delta == 0 or abs(delta) > 3
 

def is_safe_report(report, error_tolerence=0):
    error_count = 0
    if len(report) == 1:
        return 1
    else:
        direction = 'desc' if report[0] - report[1] > 0 else 'asc'
        i = 0
        while i < len(report) - 1:
            if is_unsafe_pair(report[i], report[i+1], direction):
                return 0
            else:
                i += 1
        return 1
    
with open('input.txt', 'r') as f:
    lines = [[int(c) for c in line.split()] for line in f.readlines()]

# p1
p1 = sum([is_safe_report(l) for l in lines])
print(p1)

# p2 brute force
p2 = sum([1 in [is_safe_report(l[:n] + l[n+1:]) for n in range(len(l))] for l in lines])
print(p2)
