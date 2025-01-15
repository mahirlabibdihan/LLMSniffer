t = int(input())
while t:
    n = int(input())
    arr = list( map(int,input().split()) )
    hsh = set()
    hsh1 = set(arr)
    f = 0
    for i in range(1,n+1):
        if i in hsh1:
            if arr[i-1] in hsh:
                print("Truly Happy")
                f = 1
                break
            else:
                hsh.add(arr[i-1])
    if not f:
        print("Poor Chef")
    t -= 1