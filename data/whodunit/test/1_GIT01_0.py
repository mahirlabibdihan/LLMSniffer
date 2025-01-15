for i in range(int(input())):
    count=0
    count2=0
    ar=[]
    n,m=map(int,input().split())
    for j in range(n):
        ar.append(input())
    for k in range(0,n):
        for b in range(0,m):
            if((k+b)%2==0):
                if(ar[k][b]=='R'):
                    count+=5
                else:
                    count2+=3
            else:
                if(ar[k][b]=='R'):
                    count2+=5
                else:
                    count+=3
    print(min(count,count2))
        