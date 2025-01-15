def solve(s):
    mod = 10000009
    n = len(s)
    ans = 1
    for i in range(n//2):
        if s[i] == '?' and s[n-i-1] == '?':
            ans = (ans*26)%mod
        elif s[i] == '?' or s[n-i-1] == '?':
            continue
        elif s[i] != s[n-i-1]:
            return 0
    if n%2 and s[n//2] == '?':
        ans = (ans*26)%mod
    return ans

T = int(input())
for _ in range(T):
    s = input()
    print(solve(s))