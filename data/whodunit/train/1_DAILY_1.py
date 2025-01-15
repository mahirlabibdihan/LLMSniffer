import math
n,m = map(int,input().split())
l = []
ans = 0

for i in range(m):
    t = 0
    s = str(input())
    for j in range(0,36,4):
        a = s[j:j+4]
        a+=s[53-t]
        a+=s[53-t-1]
        l.append(a)
        t+=2

    for x in range(9*i,9*i+9):
        s = l[x]
        c = s.count("0")
        if c>=n:
            cnt = math.factorial(c)//(math.factorial(n)*math.factorial(c-n))
            ans+=cnt
        

print(ans)
        
    