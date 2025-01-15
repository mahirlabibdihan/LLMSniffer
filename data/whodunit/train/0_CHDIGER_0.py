def solve():
    n, d = map(int, input().split())
    n = list(map(int, str(n)))
    if d == 1:
        print('1' * len(n))
        return
    stack = []
    for i in range(len(n)):
        while stack and stack[-1] > d and len(stack) - 1 + len(n) - i >= len(n):
            stack.pop()
        stack.append(n[i])
    while stack and stack[-1] > d:
        stack.pop()
    stack.append(d)
    print(int(''.join(map(str, stack))))

t = int(input())
for _ in range(t):
    solve()