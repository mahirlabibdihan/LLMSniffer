for i in range(int(input())):
    n = int(input());a = list(map(int,input().split()))
    print((pow(2,a.count(max(a)))-1)%(10**9 + 7))    