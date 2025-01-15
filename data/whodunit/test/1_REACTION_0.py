for _ in range(int(input())):
    r , c = map(int,input().split())
    arr = []
    for i in range(r):
        arr.append(list(map(int,input().split())))
    ans = "Stable"
    for i in range(r):
        for j in range(c):
            if ((i == 0 or i == r-1) and (j == 0 or j == c-1)) :
                if arr[i][j] > 1 :
                    ans = "Unstable"
                    break
            elif i==0 or i==r-1 or j==0 or j==c-1 :
                if arr[i][j] > 2 :
                    ans = "Unstable"
                    break
            else :
                if arr[i][j] > 3 :
                    ans = "Unstable"
                    break
            if ans == "Unstable":
                break
    print(ans)
   
    
