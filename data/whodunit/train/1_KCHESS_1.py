def neighbours(i,j):
    x = [1,-1,2,-2,1,-1,2,-2];y = [2,2,1,1,-2,-2,-1,-1]
    for k in range(8):l.add((i+x[k],j+y[k]))
    return l
for t_iter in range(int(input())):
    n = int(input());l = set()
    for n_iter in range(n):i,j = map(int,input().split());neighbours(i,j)
    a,b = map(int,input().split());x = [0,0,1,1,1,-1,-1,-1];y = [-1,1,0,1,-1,0,1,-1];flag = 0
    for k in range(8):
        if not (a+x[k],b+y[k]) in l:flag = 1;print("NO");break
    if flag == 0:print("YES")