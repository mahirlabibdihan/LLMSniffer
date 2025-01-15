for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    i=0 ; j=len(l)-1
    l=sorted(l)
    while i < j:
        print(l[i],end=" ")
        print(l[j],end=" ")
        i += 1; j -= 1
    if n%2==1: print(l[int(n/2)])
    print()
