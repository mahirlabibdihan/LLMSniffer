def sumnum(num):
    c=0
    while True:
        c+=num%10 
        num=num//10 
        if num==0:
            if c<10:
                break 
            else:
                num=c 
                c=0 
    return c 
l2=[1,2,4,8,7,5]
l5=[1,5,7,8,4,2]
for _ in range(int(input())):
    b,p=map(int,input().split())
    b=sumnum(b)
    if b==1:
        print(1)
    elif b==9:
        if p==0:
            print(1)
        else:
            print(9)
    elif b==3:
        if p==0:
            print(1)
        elif p==1:
            print(3)
        else:
            print(9)
    elif b==6:
        if p==0:
            print(1)
        elif p==1:
            print(6)
        else:
            print(9)
    elif b==8:
        r=p%2 
        if r==0:
            print(1)
        else:
            print(8)
    elif b==4:
        r=p%3
        if r==0:
            print(1)
        elif r==1:
            print(4)
        else:
            print(7)
    elif b==7:
        r=p%3
        if r==0:
            print(1)
        elif r==1:
            print(7)
        else:
            print(4)
    elif b==2:
        r=p%6
        print(l2[r])
    elif b==5:
        r=p%6
        print(l5[r])