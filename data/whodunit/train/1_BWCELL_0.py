for _ in range(int(input())):
        l=0
        r=0
        f=False
        for w in input():
                if w=="W":
                        f=True
                        continue
                if f:
                        r=r+1
                else:
                        l=l+1
        if l==r:
                            print("Chef")
        else:
                            print("Aleksa")