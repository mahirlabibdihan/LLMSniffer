for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        ma=0
        mi=l[0]
        for i in range(1,n):
            if l[i]-mi>ma:
                ma=l[i]-mi
            if l[i]<mi:
                mi=l[i]
                
        if ma==0:
            print("UNFIT")
        else:
            print(ma)   