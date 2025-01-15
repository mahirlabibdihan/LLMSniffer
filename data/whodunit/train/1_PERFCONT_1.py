s = int(input())
for tc in range(s):
    l1=list(map(int,input().split(' ')))
    n,p = l1
    l2 = list(map(int,input().split(' ')))
    k1=p//2
    k2=p//10
    c=0
    h=0
    for i in l2:
        if i>=k1:
            c=c+1
        elif i<=k2:
            h=h+1
    if c==1 and h ==2:
        print('yes')
    else:
        print('no')
