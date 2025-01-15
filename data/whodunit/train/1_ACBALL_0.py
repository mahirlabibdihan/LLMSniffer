t=int(input())
for i in range(t):
    x=input()
    y=input()
    z=''
    for i in range(len(x)):
        if x[i]==y[i]:
            if x[i]=='W':
                z+='B'
            else:
                z+='W'
        else:
            z+='B'
    print(z)