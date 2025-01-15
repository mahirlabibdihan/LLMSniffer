import math
t=int(input())
for _ in range(t):
    n=int(input())
    a_odd=0
    a_even=0
    b_odd=0
    b_even=0
    a_sum=0
    b_sum=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        if a[i]%2:
            a_odd+=1 
        else:
            a_even+=1 
        if b[i]%2:
            b_odd+=1 
        else:
            b_even+=1 
        a_sum+=a[i]
        b_sum+=b[i]
    x=(n-min(a_even,b_even)-min(b_odd,a_odd))*0.5
    print(math.floor((a_sum+b_sum)/2 - x ))
        