T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if a + b == 0 or a + c == 0 or a + d == 0 or b + c == 0 or b + d == 0 or c + d == 0 or a + b + c == 0 or a + b + d == 0 or a + c + d == 0 or b + c + d == 0 or a + b + c + d == 0:
        print("Yes")
    else:
        print("No")