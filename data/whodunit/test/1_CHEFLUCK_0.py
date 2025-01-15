for _ in range(int(input())):
    n = int(input())
    f=0
    a=n
    
    while n%7!=0:
        n-=4
    ans= a-n

    if(ans%4==0 and n>=0):
        print(n)
    else:
        print(-1)