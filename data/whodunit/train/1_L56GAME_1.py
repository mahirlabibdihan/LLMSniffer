t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(1)
    else:
        al = []
        
        for i in range(0,n):
            if a[i] % 2 != 0:
                al.append(a[i])
        
        if len(al) % 2 == 0:
            print(1)
        else:
            print(2)
    
    t -= 1