import math
for i in range(int(input())):
    h,s=map(int,input().split())
    p=s*2
    if h**2-2*p<0:
        print(-1)
        continue
    B=(((h**2+2*p)**.5)+((h**2-2*p)**.5))/2
    H=p/B
    print("%.6f %.6f %.6f"%(min(B,H),max(B,H),h))
        
    