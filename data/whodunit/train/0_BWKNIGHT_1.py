def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        total_positions = N * M
        attack_positions = 4 * max(0, N-2) * max(0, M-2)
        safe_positions = total_positions * (total_positions - 1) - attack_positions
        print(safe_positions)

solve()