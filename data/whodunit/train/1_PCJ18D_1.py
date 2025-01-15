for _ in range (int(input())):
    n,b=input().split()
    n,b=int(n),int(b)
    a=int(n/b)
    c=n-a
    if(n%b==0):
        c+=1
    print(c)


