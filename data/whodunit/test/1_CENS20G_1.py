
from collections import defaultdict
import sys
for q in range(int(sys.stdin.readline())):
    s=sys.stdin.readline()
    x1, y1=map(int,sys.stdin.readline().split())
    Q=int(sys.stdin.readline())
    dict=defaultdict(int)
    for i in s:
        dict[i]+=1
    for _ in range(Q):
        x2, y2=map(int,sys.stdin.readline().split())
        c=0
        f=0
        if x2-x1>=0:
            if dict["R"]>=x2-x1:
                c+=x2-x1
            else:
                f=1
        else:
            if dict["L"]>=x1-x2:
                c+=x1-x2
            else:
                f=1
        if y2-y1>0:
            if dict["U"]>=y2-y1:
                c+=y2-y1
            else:
                f=1
        else:
            if dict["D"]>=y1-y2:
                c+=y1-y2
            else:
                f=1
        if f==1:
            sys.stdout.write("NO")
        else:
            sys.stdout.write("YES"+" "+str(c))
        sys.stdout.write("\n")