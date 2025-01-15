def add_without_carry(a, b):
    result = 0
    multiplier = 1
    while a > 0 or b > 0:
        result += ((a % 10 + b % 10) % 10) * multiplier
        a //= 10
        b //= 10
        multiplier *= 10
    return result

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(add_without_carry(a, b))