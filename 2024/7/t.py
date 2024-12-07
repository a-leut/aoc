import itertools

def generate_combinations(n):
    return list(itertools.product(['+', '-'], repeat=n))

# Example usage
n = 3
combinations = generate_combinations(n)
print(combinations)
