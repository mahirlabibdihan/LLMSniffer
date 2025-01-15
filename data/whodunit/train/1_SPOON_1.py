for j in range(int(input())):
    r,c=map(int,input().split())
    x=[]
    for i in range(r):
        d=input().lower()
        x.append(d)
    a=0
    am=0
    for i in x:
        a=i.count("spoon")
        if(a!=0):
            print("There is a spoon!")
            am=1
            break
    if(am!=1):
        sum=""
        for k in range(c):
            for i in x:
                sum+=i[k]
            if(sum.count("spoon")!=0):
                print("There is a spoon!")
                break
        else:
            print("There is indeed no spoon!")