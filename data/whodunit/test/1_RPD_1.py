t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split(" ")))
    if(n==2):
        p = A[0]*A[1]
        d = list(map(int, list(str(p))))
        print(sum(d))
    else:
        s = []
        for j in range(n):
            for k in range(j+1,n):
                p = A[j]*A[k]
                d = list(map(int, list(str(p))))
                s.append(sum(d))
        print(max(s))