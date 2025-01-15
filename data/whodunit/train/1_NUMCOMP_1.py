t=int(input())
for i in range(t):
    a,b,n=list(map(int,input().split()))
    if (n%2)==0:
        if abs(a)>abs(b):
            print(1)
        elif abs(a)<abs(b):
            print(2)
        else:
            print(0)
            
    else:
        if a>b:
            print(1)
        elif a<b:
            print(2)
        else:
            print(0)    
      

        