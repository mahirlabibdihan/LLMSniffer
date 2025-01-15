res=""
for _ in range(int(input())):
    ans=0
    c=int(input())
    for i in range(c):
        n,m=map(int,input().split( ))
        ans^=(n+m-2)%3
    if ans:
        res+="MasterChef\n"
    else:
        res+="Football\n"
print(res)
        
        
        