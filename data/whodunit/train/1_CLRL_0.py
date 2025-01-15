for i in range(int(input())):
    n, r = map(int, input().split())
    li = list(map(int, input().split()))
    
    ans = "YES"
    least = None
    most = None
    
    for el in li:
        if el > r:
            if most == None or most > el:
                most = el
            else:
                ans = "NO"
                break
        else:
            if least == None or least < el:
                least = el
            else:
                ans = "NO"
                break
    
    print(ans)