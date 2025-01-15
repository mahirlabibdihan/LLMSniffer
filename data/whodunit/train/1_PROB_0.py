t = int(input())
while(t>0):
    t14 = input()
    t14 = list(map(int, t14.split()))
    print(float(t14[0]/(t14[0]+t14[1])))
    t=t-1