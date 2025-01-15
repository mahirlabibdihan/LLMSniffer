t= int(input())
for _ in range(t):
    h,m = map(int, input().split())
    cnt=0
    for i in range(h):
        for j in range(m):
            cnt+=1
            s = str(i)+str(j)
            for k in s:
                if k!=s[0]:
                    cnt-=1
                    break
    print(cnt)