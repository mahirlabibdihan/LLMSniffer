for _ in range(int(input())):
    k = int(input());arr = list(map(int,input().split()));d=0.5
    for i in arr: d = d*2 - i
    print("Yes") if(d == 0) else print("No")