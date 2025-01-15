t = int(input())
for i in range(t):
    s,sg,fg,d,T = map(int,input().split())
   

    
    v = s + (d*180)/T

    if abs(sg-v) > abs(fg-v):
        print("FATHER")
    elif abs(sg-v) < abs(fg-v):
        print("SEBI")
    else:
        print("DRAW")