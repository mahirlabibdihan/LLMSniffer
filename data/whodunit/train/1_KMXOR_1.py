T=int(input())
def powe(a):
    t7=0
    while(a>1):
        a=a//2
        t7+=1
    return t7
for _ in range(T):
    n,k=list(map(int,input().split()))
    if(n==1):
        print(k)
    elif(n==2):
        if(k==1):
            print(1,1)
        elif(k==2):
            print(2,1)
        else:
            print(2**powe(k),2**powe(k)-1)
    else:
        if(k==1):
            for i in range(n):
                print(1,end=" ")
            print()
        elif(k==2):
            print(2,end=" ")
            for i in range(n-1):
                print(1,end=" ")
            print()
        elif(k==3):
            if(n%2==0):
                print(2,1,end=" ")
                for i in range(n-2):
                    print(1,end=" ")
                print()
            else:
                print(3,end=" ")
                for i in range(n-1):
                    print(1,end=" ")
                print()
        else:
            if(n%2==0):
                print(2**powe(k),2**powe(k)-1,end=" ")
                for i in range(n-2):
                    print(1,end=" ")
                print()
            else:
                print(2**powe(k),2**powe(k)-2,end=" ")
                for i in range(n-2):
                    print(1,end=" ")
                print()
