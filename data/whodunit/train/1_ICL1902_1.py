import math
for t in range(int(input())):
    n=int(input())
    c=0
    while(n!=0):
        s=int(math.sqrt(n))
        c+=1
        n=n-(s*s)
    print(c)
        