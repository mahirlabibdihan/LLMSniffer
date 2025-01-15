N, X = map(int, input().split())
A = list(map(int, input().split()))
lst = []
s = 0
psum = A[:]
for i in range(1, N):
    psum[i] += psum[i-1]
m = -9999999
for i in range(0, N):
    for j in range(i, N):
        m = max(m, psum[j] - psum[i] + A[i])
print(psum[-1] - m + m / X)