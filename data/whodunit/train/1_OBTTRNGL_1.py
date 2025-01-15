try:
    for _ in range(int(input())):
        k,a,b=map(int, input().split())
        if a>b:
            t=a
            a=b 
            b=t
        if b-a == k/2:
            print(0)
        elif b-a < k/2:
            print(b-a-1)
        else:
            print(k+a-b-1)
except EOFError: pass

            