def main():
    for _ in range(int(input())):
        n,m=list(map(int,input().split()))
        if n==1:
            print(m*(m-1))
        elif m==1:
            print(n*(n-1))
        else:
            print((n*m)*(n*m-1)-4*((m-2)*(n-1)+(m-1)*(n-2)))
if __name__=="__main__":
    main()
