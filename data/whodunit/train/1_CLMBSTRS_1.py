sli=['0']*1000001
sli[0]=1
sli[1]=1

for i in range(2,1000001):
    sli[i]=(sli[i-2]+sli[i-1])%1000000007

for _ in range(int(input())):
    n,g=map(int,input().split())

    if g==bin(sli[n]).count('1'):
        print('CORRECT')
    else:
        print('INCORRECT')
