t=int(input())
for i in range(t):
    n=int(input())
    count=0

    for ppoo in range(n):
        s,j=map(int,input().split())
        if j-s>5:
            count+=1
    print(count)
    
    