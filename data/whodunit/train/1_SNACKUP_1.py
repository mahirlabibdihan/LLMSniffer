tc = int(input())
for _ in range(tc):
    n = int(input())
    N = range(1,n+1)
    print(n)
    
    for i in range(1,n+1):
        print(n)
        for j in range(1,n+1):
            print(j,N[(i+j-1)%n],N[(i+j)%n])
    