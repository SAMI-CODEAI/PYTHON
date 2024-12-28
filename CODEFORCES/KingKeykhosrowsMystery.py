from math import gcd

def find_smallest_m(a, b):
    # Calculate LCM using the formula lcm(a, b) = (a * b) // gcd(a, b)
    return (a * b) // gcd(a, b)

# Read the number of test cases
t = int(input())
results = []

for _ in range(t):
    # Read a and b for each test case
    a, b = map(int, input().split())
    # Compute the smallest m and store the result
    results.append(find_smallest_m(a, b))

# Output all results
print("\n".join(map(str, results)))
