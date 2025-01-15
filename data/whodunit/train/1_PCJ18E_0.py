for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    l = sorted(arr)
    i = 0
    j = 0
    while(i<n and j<n):
        if l[i]==arr[j]:
            i+=1
            j+=1
        else:
            j+=1
    print(n-i)