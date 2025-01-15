def my_func(n,m):
    l = []
    for j in range(n):
        k = list(map(int,input().split()))
        l.append(k)
    temp = 1
    for j in  range(n):
        for k in range(m):
          if j == 0:
            if j == 0 and k == 0:
                if l[j][k] == -1: l[j][k] = temp
                else: temp = l[j][k]
            else:
                if l[j][k] == -1: l[j][k] = temp
                else: temp = l[j][k]
          else:
              if l[j][k] == -1:
                 if k != 0: l[j][k] = max(l[j-1][k],l[j][k-1])
                 else: l[j][k] = l[j-1][k]
    flag = 0
    for i in range(m):
        ans = []
        for j in range(n):
            ans.append(l[j][i])
        if sorted(ans) == ans: continue
        else:
            flag = 1
            break
    for i in range(n):
        k = l[i]
        if sorted(k) == k: continue
        else:
            flag = 1
            break
    if flag == 0:
       for i in range(n):
           print(*l[i])
    else: print(-1)
if __name__ == "__main__":
    for i in range(int(input())):
        n,m = map(int,input().split())
        my_func(n,m)