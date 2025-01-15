for i in range(int(input())):
    n=int(input())
    l=[]
    h=1
    v=1
    win=0
    for i in range(n):
        x=input().strip()
        if len(x)>=3:
            if x[-3:]=='man':
                h=h+1
            else:
                v=v+1
        else:
            v=v+1
        if win==0:
            if v+2<=h:
                win=1
            elif h+3<=v:
                win=2
    if win==0:
        print('draw')
    elif win==1:
        print('superheroes')
    elif win==2:
        print('villains')