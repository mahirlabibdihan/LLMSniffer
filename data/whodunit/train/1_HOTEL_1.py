try:
    import numpy as np
    for _ in range(int(input())):
        n = int(input())
        arrival = np.array(list(map(int,input().split())))
        departure = np.array(list(map(int,input().split())))
        
        arr = [0]*1000
        arr = np.array(arr)
        
        for i in range(n):
            arr[arrival[i]:departure[i]]+=1
        
        print(max(arr))
except EOFError:
    pass