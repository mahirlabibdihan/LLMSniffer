def solve():
    T = int(input().strip())
    for _ in range(T):
        S = input().strip()
        x1, y1 = map(int, input().strip().split())
        Q = int(input().strip())
        queries = [list(map(int, input().strip().split())) for _ in range(Q)]
        R = L = U = D = 0
        for s in S:
            if s == 'R':
                R += 1
            elif s == 'L':
                L += 1
            elif s == 'U':
                U += 1
            elif s == 'D':
                D += 1
        for q in queries:
            x2, y2 = q
            dx = x2 - x1
            dy = y2 - y1
            if dx >= 0 and dy >= 0 and R >= dx and U >= dy:
                print("YES", max(dx, dy))
            elif dx <= 0 and dy <= 0 and L >= abs(dx) and D >= abs(dy):
                print("YES", max(abs(dx), abs(dy)))
            elif dx >= 0 and dy <= 0 and R >= dx and D >= abs(dy):
                print("YES", max(dx, abs(dy)))
            elif dx <= 0 and dy >= 0 and L >= abs(dx) and U >= dy:
                print("YES", max(abs(dx), dy))
            else:
                print("NO")

solve()