t = int(input())

for i in range(t):
    n, k, l = map(int, input().split())
    l -= 1
    a = []
    while l != 0:
        a.insert(0, l % k)
        l //= k 
    while len(a) != n:
        a.insert(0, 0)
    for j in a:
        print(j + 1, end=" ")
    print()