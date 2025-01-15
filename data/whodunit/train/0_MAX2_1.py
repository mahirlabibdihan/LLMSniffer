def max_power_of_two(N, X):
    return len(X) - len(X.rstrip('0'))

N = int(input().strip())
X = input().strip()
print(max_power_of_two(N, X))