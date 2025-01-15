t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = {}
    b = {}
    l = []
    for i in range(n):
        a[i] = 0
    for i in range(m):
        b[i] = 0
    for i in range(n):
        l.append(input())
    for i in range(n):
        for j in range(m):
            if l[i][j] == '1':
                a[i]=1
                b[j]=1
    if sum(a.values()) + sum(b.values()) == 0:
        for i in range(n):
            for j in range(m):
                print(-1,end=' ')
            print()
    else:
      
        ans = []
        for i in range(n):
            ans.append([0]*m)
        for i in range(n):
            for j in range(m):
                if l[i][j] == '1':
                    ans[i][j] = 0
                else:
                    if(a[i] or b[j]):
                        ans[i][j] = 1
                    else:
                        ans[i][j] = 2
        for i in range(n):
            for j in range(m):
                print(ans[i][j],end=" ")
            print()
                
            
        
