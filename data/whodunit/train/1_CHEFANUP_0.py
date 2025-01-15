import sys
sys.setrecursionlimit(10**6)



for _ in range(int(input())):
    n, k, l = [int(x) for x in input().split()]
    l = l - 1
    ans = []
    while l:
        ans.append(l % k)
        l = l//k
    

    while len(ans) != n:
        ans.append(0)
    
    ans = ans[::-1]
    ans = [x+1 for x in ans]
    
    print(*ans)
    
    
    
    