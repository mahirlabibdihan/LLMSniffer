for _ in range(int(input())):
    N,k=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    print(sum([arr[i]*brr[i] for i in range(len(arr))])+(max(map(abs,brr)))*k)