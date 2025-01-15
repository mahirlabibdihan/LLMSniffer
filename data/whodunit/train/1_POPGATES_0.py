for i in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(str,input().split()))
    head_cnt = 0
    while k:
        t = arr.pop()
        if t == "H":
            for i in range(len(arr)):
                if arr[i] == "T":
                    arr[i] = "H"
                else:
                    arr[i] = "T"
        k-=1
    for i in range(len(arr)):
        if arr[i] == "H":
            head_cnt += 1 
    print(head_cnt)