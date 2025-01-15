from operator import xor
def find_xor(n):
    m=n%4
    if m==0:
        return n
    elif m==1:
        return 1
    elif m==2:
        return n+1
    elif m==3:
        return 0;
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    t=xor(find_xor(l-1),find_xor(r))
    if t%2==0:
        print("Even")
    else:
        print("Odd")
    
