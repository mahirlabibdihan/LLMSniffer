for _ in range(int(input())):
    n, m, k = map(int, input().split())
    
    x = n % m
    flag = False
    cnt = 0
    
    while n > 0:
        if n % m == 0:
            flag = True
            break
        cnt += 1
        n -= k
        
    if flag:
        print(cnt)
    else:
        print(-1)