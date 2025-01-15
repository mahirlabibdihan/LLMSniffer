MOD = 10000009

def solve(s):
    n = len(s)
    cnt = 0
    for i in range(n//2):
        if s[i] == '?' and s[n-i-1] == '?':
            cnt += 1
        elif s[i] != '?' and s[n-i-1] != '?' and s[i] != s[n-i-1]:
            return 0
    if n % 2 and s[n//2] == '?':
        cnt += 1
    return pow(26, cnt, MOD)

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(solve(s))