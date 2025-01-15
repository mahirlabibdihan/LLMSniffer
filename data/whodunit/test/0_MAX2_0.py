def max_power_of_two(N, X):
    binary_num = int(X, 2)
    power = 0
    while binary_num % 2 == 0:
        binary_num /= 2
        power += 1
    return power

N = int(input().strip())
X = input().strip()
print(max_power_of_two(N, X))