t=int(input())
while(t>0):
    s=input()
    a=[]
    for x in range(len(s)-1):
        if s[x:x+2] not in a:
            a.append(s[x:x+2])
    print(len(a))
    t-=1