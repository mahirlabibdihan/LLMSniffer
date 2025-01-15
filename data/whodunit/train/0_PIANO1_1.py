def calculate_plays(s, N):
    total_keys = 12 * N
    pattern_length = s.count('T') * 2 + s.count('S')
    return total_keys - pattern_length + 1

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    N = int(input().strip())
    print(calculate_plays(s, N))