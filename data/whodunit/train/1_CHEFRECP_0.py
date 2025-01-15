
def check(L, n):
    count = dict()
    
    for i in range(n):
        a = L[i]
        count[a] = count.setdefault(a, 0) + 1 
        if count[a]>1:
            if L[i-1] !=L[i]:
                return False
    t = tuple(count.values())
    if len(t)!=len(set(t)):
        return False
    return True

for i in range(int(input())):
    n = int(input())
    L = list(map(int,input().split()))
    ch = check(L, n)
    if ch:
        print("YES")
    else:
        print("NO")