import math
st=''
def func(n,a,k):
    s=(n-2)*180
    y=n*(n-1)
    x=a*y+2*(k-1)*(s-a*n)
    g=math.gcd(x,y)
    x,y=x//g,y//g
    return(str(str(x)+' '+str(y)))


for _ in range(int(input())):
    n,a,k=map(int,input().split())
    #n = int(input())
    #l1=[]
    #inp=input().split()
    #s=input()
    #l1=list(map(int,input().split()))
    #l2 = list(map(int, input().split()))
    #l1=input().split()
    #l2=input().split()
    st+=str(func(n,a,k))+'\n'

print(st)

