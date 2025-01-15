for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    for j in range(n):
        k = 1
        for qq in range(n):
            if a[j][qq] == 0:
                k = 0
                break
        if k==1:
            print("NO")
            break
    if k==0:
         for l in range(n):
             k=1
             for q in range(n):
                 if a[q][l]==0:
                     k=0
                     break
             if k!=0:
                 print("NO")
                 break
    if k==0:
        print("YES")