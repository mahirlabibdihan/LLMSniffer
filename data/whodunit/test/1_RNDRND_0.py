m,n = map(int,input().split())
t=[int(x) for x in input().split()]
ans=[]
for i in range(1,(m)):
    td=t.copy()
    k,cnt,l =1,1,[1]
    while len(td)!=0:
        if k in td:
            td.remove(k)
        if len(td)==0:
            break
        k+=i
        cnt+=1
        if k>m:
            k=k-m
        if k in l:
            cnt=10000000000000
            break
        l.append(k)
    ans.append(cnt)
# print(ans)
print(min(ans))