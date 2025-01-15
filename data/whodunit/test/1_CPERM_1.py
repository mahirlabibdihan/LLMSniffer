MOD=10**9+7
for _ in range(int(input())):
    a=int(input())
    if a==0 or a==1 or a==2:
        print(0)
    else:
        print((pow(2,a-1,MOD)-2)%(MOD))