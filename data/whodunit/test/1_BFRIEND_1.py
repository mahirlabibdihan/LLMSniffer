T = int(input())
for i in range(T):
    N, a, b, c = map(int, input().split())
    F = list(map(int, input().split()))
    F.sort()
    l = []
    for i in range(len(F)):
        s = 0
        s += abs(F[i]-b)
        s += c
        s += abs(F[i]-a)
        l.append(s)
    print(min(l))