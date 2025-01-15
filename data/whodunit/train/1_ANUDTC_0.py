for _ in range(int(input())):
    n = int(input());
    q1=q2=q3=0;
    if 360%n==0:
        print('y', end=" ");
    else:
        print('n', end=" ");
    if n<=360:
        print('y', end=" ");
    else:
        print('n', end=" ");
    if n*(n+1)//2<=360:
        print('y', end=" ");
    else:
        print('n', end=" ");
    print();