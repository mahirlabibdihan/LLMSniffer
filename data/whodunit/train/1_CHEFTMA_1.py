for _ in range(int(input())):
    n,k,m = list(map(int,input().split()))
    planned = list(map(int,input().split()))
    completed = list(map(int,input().split()))
    white = list(map(int,input().split()))
    black = list(map(int,input().split()))
    remaining = [ planned[i]-completed[i] for i in range(n)]
    rem = sorted(remaining,reverse=True)
    sub =sorted(white+black,reverse=True)
    t = k+m
    j = 0
    for i in range(n):
        while j<t:
            if sub[j]<=rem[i]:
                rem[i] = rem[i]-sub[j]
                j+=1
                break
            j+=1
        if j==t:
            break
    print(sum(rem))