a = int(input())
for i in range(a):
    b = int(input())
    if b%8==0:
        print(str(b-1) + 'SL')
    elif b%8==7:
        print(str(b+1) + 'SU')
    elif b%8==1:
        print(str(b+3) + 'LB')
    elif b%8==2:
        print(str(b+3) + 'MB')
    elif b%8==3:
        print(str(b+3) + 'UB')
    elif b%8==4:
        print(str(b-3) + 'LB')
    elif b%8==5:
        print(str(b-3) + 'MB')
    elif b%8==6:
        print(str(b-3) + 'UB')