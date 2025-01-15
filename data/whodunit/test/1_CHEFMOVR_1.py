T = int(input())
for i in range(T):
    N, D = map(int,input().split())
    arr = list(map(int,input().split()))
    
    total = sum(arr)
    if(total % len(arr) != 0):
        print(-1)
    else:
        div = total // len(arr)
        j = 0
        count = 0
        while j + D < len(arr):
            if (arr[j] < div):
                diff = div - arr[j]
                count += diff
                arr[j] += diff
                arr[j+D] -= diff
            elif (arr[j] > div):
                diff = arr[j] - div
                count += diff
                arr[j] -= diff
                arr[j+D] += diff  
            j+=1
        while j < len(arr):
            if arr[j] != div:
                count = -1
                break
            j+=1
        print(count)