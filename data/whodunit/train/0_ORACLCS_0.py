T = int(input())
for _ in range(T):
    n = int(input())
    strings = [input() for _ in range(n)]
    min_a = min(s.count('a') for s in strings)
    min_b = min(s.count('b') for s in strings)
    print(min_a + min_b)