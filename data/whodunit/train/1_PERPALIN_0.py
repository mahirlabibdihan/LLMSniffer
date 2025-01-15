for i in range(int(input())):
    n,p = map(int,input().split())
    if p>2:
        lst = ['a']
        
        for j in range(p-2):
            lst.append('b')
        lst.append('a')
        print((''.join(lst))*(n//p))

    else:
        
        print("impossible")