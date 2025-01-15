try:
    def fun(t):
        for i in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=set(a)
            print(len(b))
    t=int(input())
    fun(t)
except:
    pass