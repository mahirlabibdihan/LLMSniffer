if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n1,n2,m = map(int,input().split())
        temp = min(n1,n2)
        # if temp > sum of m numbers then
        count = 0
        total = m*(m+1)//2
        if total<temp:
            count = total
        else:
            count = temp
        ans = n1+n2-2*count
        print(ans)
            

    