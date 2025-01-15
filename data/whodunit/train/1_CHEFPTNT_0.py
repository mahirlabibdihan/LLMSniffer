for _ in range(int(input())):
    n,m,x,k = map(int,input().split())
    string1 =input()
    if k==0 or k<n:
            print('no')
            continue
        
    kaam=n
    emp=k
    
    eval=string1.count('E')
    oval=string1.count('O')
    ww='odd'
    
    for _ in range(0,m):
        if ww=='odd':
                kaam=kaam - min(min(oval,x),emp)
                oval-=min(min(oval,x),emp)
                emp=emp-min(min(oval,x),emp)
                ww='even'
        else:
                kaam=kaam - min(min(eval,x),emp)
                
                k=k-min(min(eval,x),emp)
                eval -= min(min(eval,x),emp)
                ww='odd'
    if kaam<=0:
        print('yes')
    else:
        print('no')