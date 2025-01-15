T = int(input())
for _ in range(T):
    U, V = map(int, input().split())
    if U > V:
        print((U*(U+1))//2 + 1)
    else:
        print((V*(V+1))//2 + 1)