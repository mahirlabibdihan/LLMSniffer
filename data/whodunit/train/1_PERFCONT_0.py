for tc in range(int(input())):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    cakewalk,hard=0,0
    for i in range(n):
        if p//2<=a[i]:
            cakewalk+=1 
        if p//10>=a[i]:
            hard+=1 
    if cakewalk==1 and hard==2:
        print("yes")
    else:
        print("no")