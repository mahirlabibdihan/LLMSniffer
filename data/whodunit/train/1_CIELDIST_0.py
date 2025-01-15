for i in range(int(input())):
    d1,d2,d=map(int,input().split())
    print(max(0,d-d1-d2,d1-d-d2,d2-d-d1))