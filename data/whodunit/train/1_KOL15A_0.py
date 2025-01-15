t=int(input())
while t>0:
    t=t-1
    c=0
    n=input()
    for i in n:
        if i.isdigit()==True:
            c=c+int(i)
    print(c)