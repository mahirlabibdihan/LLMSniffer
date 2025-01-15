for _ in range(int(input())):
    s=input()
    a=[]
    for i in s:
        a.append(i)
    aa=set(a)
    if len(aa)==len(a):
        print('no')
    else:
        print('yes')