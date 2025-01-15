for t in range(int(input())):
    n,m=map(int,input().split())
    mat=[ ]
    dots=0
    has=0
    for i in range(n):
        l=list(input())
        mat.append(l)
        dots+=l.count('.')
        has+=l.count('#')
    for i in range(n):
        if i+1==n:
            break
        for j in range(m):
            if j+1==m:
                break
            e1=mat[i][j]
            e2=mat[i+1][j]
            e3=mat[i][j+1]
            e4=mat[i+1][j+1]
            if e1=='#'or e2=='#' or e3=='#' or e4=='#':
                continue
            else:
                mat[i][j]='g'
                mat[i+1][j]='g'
                mat[i][j+1]='g'
                mat[i+1][j+1]='g'
    org=0
    for i in range(n):
        org+=mat[i].count('g')
    if org==dots:
        print("YES")
    else:
        print("NO")
    
    