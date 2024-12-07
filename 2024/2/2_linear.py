def is_unsafe_pair(n, p, direction):
    delta = n - p
    return delta > 0 and direction == 'asc' or delta < 0 and direction == 'desc' \
            or delta == 0 or abs(delta) > 3
 

def is_safe_report_linear(report):
    # Helper to determine direction
    def get_direction(a, b):
        return 'asc' if a < b else 'desc'
    
    n = len(report)
    if n <= 1:
        return True
    
    # Step 1: Precompute safety information
    # Check safety between pairs
    unsafe = [False] * (n - 1)  # Unsafe pair indicators
    direction = get_direction(report[0], report[1])
    for i in range(n - 1):
        if is_unsafe_pair(report[i], report[i + 1], direction):
            unsafe[i] = True

    # Step 2: Check if removing any single element makes the report safe
    unsafe_count = sum(unsafe)
    if unsafe_count == 0:  # Already safe
        return True

    # Evaluate removing each element
    for i in range(n):
        # If removing i fixes all issues, it's valid
        if i == 0:  # Removing the first element
            if not unsafe[0]:
                return True
        elif i == n - 1:  # Removing the last element
            if not unsafe[-1]:
                return True
        else:  # Removing an intermediate element
            if not (unsafe[i - 1] or unsafe[i]):
                return True

    return False


# Optimized p2 computation
with open('input.txt', 'r') as f:
    lines = [[int(c) for c in line.split()] for line in f.readlines()]

p2 = sum(is_safe_report_linear(l) for l in lines)
print(p2)
