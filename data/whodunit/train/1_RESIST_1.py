def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
for _ in range(int(input())):
    n,m = map(int,input().rstrip().split())
    num  = 1
    den = 1
    for i  in range(2,n+1):
        num  = (num+den)%m
        den = (num + den)%m
    #g = gcd(num,den)

    print(str((num)%m)+"/"+str((den)%m))
    