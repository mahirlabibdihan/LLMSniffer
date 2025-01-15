for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        st=input().split()
        for j in range(m):
            val=int(st[j])
            arr.append(val)
    arr.sort(reverse=True)
    cy=0
    ge=0
    for i in range(n*m):
        if i%2==0:
            cy+=arr[i]
        else:
            ge+=arr[i]
    if cy==ge:
        print("Draw")
    elif cy>ge:
        print("Cyborg")
    else:
        print("Geno")
