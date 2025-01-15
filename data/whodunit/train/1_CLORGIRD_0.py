for _ in range(int(input())):
    n,m=map(int,input().split(" "))
    matrix=[]
    num_dots=0
    num_has=0
    for i in range(n):
        temp=list(input())
        matrix.append(temp)
        num_dots+=temp.count('.')
        num_has+=temp.count('#')
    
    for i in range(n):
        if i+1==n:
            break
        for j in range(m):
            if j+1==m:
                break
            elem1=matrix[i][j]
            elem2=matrix[i][j+1]
            elem3=matrix[i+1][j]
            elem4=matrix[i+1][j+1]

            if elem1=='#' or elem2=='#' or elem3=='#' or elem4=='#':
                pass
            else:
                matrix[i][j]='c'
                matrix[i][j+1]='c'
                matrix[i+1][j]='c'
                matrix[i+1][j+1]='c'
    
    num_cs=0
    for i in range(n):
        num_cs+=matrix[i].count('c')
    
    if num_dots==num_cs:
        print("YES")
    else:
        print("NO")