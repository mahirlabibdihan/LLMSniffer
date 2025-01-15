for _ in range(int(input())):
    n=int(input())
    d={}
    for i in range(n):
        name,vote=input().split()
        d[name]=vote
    c=0
    for name in d:
        if d[name]=='+':
            c+=1
        else:
            c-=1 
    
    print(c)