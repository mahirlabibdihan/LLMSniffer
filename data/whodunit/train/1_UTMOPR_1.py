try:
    for _ in range(int(input())):
        N, K = map(int, input().split(" "))
        l = list(map(int, input().split(" ")))
        s = sum(l)
        if(s % 2 == 0 and K == 1):
            print("odd")
        else:
            print("even")
except:
    pass