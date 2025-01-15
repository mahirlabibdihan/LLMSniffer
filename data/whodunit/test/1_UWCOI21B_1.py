
import bisect

num,m=map(int,input().split())
v=list(map(int,input().split()))
w=list(map(int,input().split()))
v.sort()
w.sort()
a=0
for i in w:
    f=bisect.bisect_right(v,i)
    if(f==0 and v[f]>i):
        a=a+num
print(a)