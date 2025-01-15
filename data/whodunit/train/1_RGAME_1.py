
def main():
    for _ in range(int(input())):
        t,b,c=0,1,10**9+7
        l=int(input())
        a=list(map(int,input().split()))
        p=a[0]*2
        for i in range(1,l+1):
            t=(t*2+p*a[i])%c
            b=(b*2)%c
            p=(p+a[i]*b)%c
        print(t)
if __name__=="__main__":
    main()