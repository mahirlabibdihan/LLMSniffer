for _ in range(int(input())):
    p,s=map(int,input().split())
    b=(p-(p**2-24*s)**(0.5))/12
    l=p/4-2*b
    print("%.2f"%(l*b*b))
