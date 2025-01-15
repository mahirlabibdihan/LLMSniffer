try:
    t=int(input())
    while t!=0:
        s=input()
        c1=0
        c2=0
        for i in range(0,len(s),1):
            if i%2==0:
                if s[i]=="-":
                    c2+=1
                else:
                    c1+=1
            else:
                if s[i]=="+":
                    c2+=1
                else:
                    c1+=1
        if c1>=c2:
            print(c2)
        else:
            print(c1)
        t=t-1
except:
    pass
