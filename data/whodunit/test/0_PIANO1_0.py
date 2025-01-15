def solve():
    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        N = int(input().strip())
        total_keys = 12 * N
        pattern_length = s.count('T') * 2 + s.count('S')
        print(total_keys - pattern_length + 1)

solve()