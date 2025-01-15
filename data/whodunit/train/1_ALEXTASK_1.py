import math

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    m = (s[0]*s[1])//math.gcd(s[0],s[1])
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            x = (s[i]*s[j])//math.gcd(s[i], s[j])
            if x < m:
                m = x
    print(m)