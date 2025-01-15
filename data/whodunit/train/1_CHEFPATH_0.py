for i in range(int(input())):
    m,n=map(int,input().split())
    if(n%2==0 or m%2==0):
        if(n==1 and m>2) or (m==1 and n>2):
            print("No")
        else:
            print("Yes")
    else:
        print("No")