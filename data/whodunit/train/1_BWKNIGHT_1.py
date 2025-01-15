testcases = int(input())
for i in range(testcases):
    n, m = input().split()
    n = int(n)
    m = int(m)
    # we always take n as the greater one
    if(n < m):
        n, m = m, n
    if(n==1 or m == 1):
        print(n*(n-1))
    else :
        out = (n*m)*(n*m-1) - 4*((n-2)*(m-1) + (n-1)*(m-2))
        print(out) 
