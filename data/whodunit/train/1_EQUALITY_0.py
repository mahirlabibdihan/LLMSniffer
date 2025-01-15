def main():
    t = int(input())
    for __ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        s = sum(a)//(n-1)
        print(*[abs(x-s) for x in a])
if __name__ == '__main__':
    main()
