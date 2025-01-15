from collections import Counter
n = int(1e5+1)
pf = [0] * n
for i in range(2, n):
    if pf[i] == 0:
        for j in range(i, n, i):
            pf[j] += 1
            
test = int(input())
for _ in range(test):
    input()
    cnt = Counter(map(int, input().split()))
    s = lambda i: sum(cnt[j] for j in range(i, n, i))
    print(max(s(i) * pf[i] for i in range(2, n)))