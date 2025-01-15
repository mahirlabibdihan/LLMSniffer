for _ in range(int(input())):
    a,b=map(list,input().split())
    if len(a)<len(b):
        for i in range(len(b)-len(a)):
            a.insert(0,0)
    elif len(a)>len(b):
        for i in range(len(a)-len(b)):
            b.insert(0,0)
    s=''
    for i in range(len(a)):
        s+=str(int(a[i])+int(b[i]))[-1]
    print(int(s))