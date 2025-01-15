for i in range(int(input())):
    l1=list(input().split())
    l2=list(input().split())
    a=0
    for i in l1:
        if i in l2:
            a+=1
    if a>=2:
        print("similar")
    else:
        print("dissimilar")