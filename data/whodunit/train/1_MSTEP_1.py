for i in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        t=[int(i) for i in input().split()]
        arr.append(t)
    x=[0]*(n**2)
    y=[0]*(n**2)   
    for i in range(n):
        for j in range(n):
            x[arr[i][j]-1]=i+1
            y[arr[i][j]-1]=j+1
    s=0 
    for i in range(n**2-1):
        s+=abs(x[i]-x[i+1])+abs(y[i]-y[i+1])
    print(s)            
