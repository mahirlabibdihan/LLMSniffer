t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    squareValues = input().split()
    A = list(map(int, squareValues))

    for i in range(n-k-1, -1, -1):
        A[i] = A[i] + A[i+k]
    
    print(max(A)) 
    
    
    
            
        