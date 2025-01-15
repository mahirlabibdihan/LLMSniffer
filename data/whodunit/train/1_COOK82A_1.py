for _ in range(int(input())):
    d={}
    for i in range(4):
        x = input().split()
        d[x[0]]=int(x[1])
    
    if d["Barcelona"]>d["Eibar"] and d["RealMadrid"]<d["Malaga"]:
        print("Barcelona")
    else:
        print("RealMadrid")