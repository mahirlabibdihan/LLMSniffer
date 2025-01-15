t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x>=0:
        if not x%2:
            if y>0:
                if y>=2+x and not y%2:
                    print('YES')
                else:
                    print('NO')
            else:
                if -1*y>=x and not y%2:
                    print('YES')
                else:
                    print('NO')
        else:
            if y<=x+1 and y>=-1*(x-1):
                print('YES')
            else:
                if y>=0 and y>=x+1 and not y%2:
                    print('YES')
                elif y<0 and -1*y>=x+1 and not y%2:
                    print('YES')
                else:
                    print('NO')
    else:
        if x%2:
            x=-1*x
            if y>0:
                if y>=1+x and not y%2:
                    print('YES')
                else:
                    print('NO')
            else:
                if -1*y>=1+x and not y%2:
                    print('YES')
                else:
                    print('NO')
        else:
            x=-1*x
            if y>=-1*x and y<=x:
                print('YES')
            else:
                if y<0:
                    y=-1*y
                if not y%2 and y>=x:
                    print('YES')
                else:
                    print('NO')
            
