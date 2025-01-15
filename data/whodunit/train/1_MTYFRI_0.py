tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    motu = [a[0]]
    tomu = []
    
    for i in range(1, len(a)):
        if i % 2 == 0:
            motu.append(a[i])
        else:
            tomu.append(a[i])
    
    if sum(tomu) > sum(motu):
        print("YES")
        continue
    
    else:
        motu.sort(reverse = True)
        tomu.sort()
        
        for i in range(len(tomu)):
            if motu[i] > tomu[i] and k:
                motu[i], tomu[i] = tomu[i], motu[i]
                k -= 1
            if k == 0:
                break
            
        if sum(motu) < sum(tomu):
            print("YES")
        else:
            print("NO")