import math
for _ in range(int(input())):
    n,m,x,k=map(int,input().split())
    s=input()
    ecount=int(s.count('E'))
    ocount=int(s.count('O'))
    emonth=math.floor(m/2)
    omonth=math.ceil(m/2)

    if (min(ocount,x*omonth)+min(ecount,x*emonth))>=n:
        print('yes')
    else:
        print('no')

