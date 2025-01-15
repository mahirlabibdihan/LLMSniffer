for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mc=a.count(max(a))
    print((2**mc -1)%(10**9+7))
