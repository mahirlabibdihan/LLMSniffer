for _ in range(int(input())):
    s,sg,fg,d,t=map(int,input().split())
    s+=(180*d)/t
    if abs(sg-s)==abs(fg-s):
        print('DRAW')
    elif abs(sg-s)<abs(fg-s):
        print('SEBI')
    elif abs(sg-s)>abs(fg-s):
        print('FATHER')
