for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    b=list(filter(lambda x: x%2!=0,l))
    if(len(l)==1):
        print(1)
    elif(len(b)%2==0):
        print(1)
    else:
        print(2)