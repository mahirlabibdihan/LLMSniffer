test=int(input())
for _ in range(test):
    n=int(input())
    my=-1
    op=-1
    for i in range(n):
        a,x,y=map(int,input().split())
        if(a==1):
            print("YES")
            my=x
            op=y
        else:
            if(x==y):
                print("YES")
                my=x
                op=y
            elif(my!=-1 and op!=-1):
                if(max(x,y)>=max(my,op) and min(x,y)<max(my,op)):
                    if(my>op):
                        my=max(x,y)
                        op=min(x,y)
                    else:
                        op=max(x,y)
                        my=min(x,y)
                    print("YES")
                else:
                    print("NO")
            elif(my==-1 and op==-1):
                print("NO")