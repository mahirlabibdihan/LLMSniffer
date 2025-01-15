mod = 10 ** 9 + 7

def fp(a, b):
    ans = 1
    while b > 0:
        if b & 1:
            ans = ans * a % mod
        b >>= 1
        a = a * a % mod
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pair = list(enumerate(arr))
    pair.sort(key=lambda x: x[1])
    ans = [0] * n
    for i in range(n):
        s = 0
        a = n-i-1
        b = a * (a+1) // 2
        p = fp(2, i)
        s = (s + p - 1) % mod
        s = (s + b * p % mod) % mod
        ans[pair[i][0]] = s
    print(' '.join(map(str, ans)))
        
