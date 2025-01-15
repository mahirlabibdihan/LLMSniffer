from heapq import *
def solve():
    n, d = map(int, input().split())
    n = list(str(n))
    n.append('0')
    heap = []
    ans = []
    for i in range(len(n)):
        while heap and heap[0] > n[i]:
            ans.append(heappop(heap))
        heappush(heap, n[i])
    while heap:
        ans.append(heappop(heap))
    ans = int(''.join(ans))
    while True:
        temp = ans
        while temp and temp % 10 >= d:
            temp //= 10
        if temp == 0:
            break
        ans = temp * 10 + d
    print(ans)

t = int(input())
for _ in range(t):
    solve()