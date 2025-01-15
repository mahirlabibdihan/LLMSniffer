for _ in range(int(input())):
    a = []
    b = []
    for i in range(26):
        a.append(0)
        b.append(0)
    sa = input()
    sb = input()
    for i in range(len(sa)):
        a[ord(sa[i])-97]+=1
        b[ord(sb[i])-97]+=1
    f=0
    s = 0
    for i in range(26):
        if b[i]==0 and a[i]>=2:
            f=1
            break
        elif b[i]==0 and a[i]==1:
            s=1
    if f==1:
        print('A')
    elif s==1:
        z = 0
        for i in range(26):
            if b[i]>0 and a[i]==0:
                z=1
                break
        if z==1:
            print('B')
        else:
            print('A')
    else:
        print('B')