# for _ in range(int(input())):
#     n=int(input())
#     s,k=input().split()
#     c=0
#     lst=[]
#     for i in range(n):
#         if(lst[i]==k):
#             c+=(i+1)
#             lst.append(i+1)
#         elif lst:
#             c+=lst[-1]
#     print(c)
    
for _ in range(int(input())):
    n=int(input())
    s,x=input().split()
    count=0
    t=[]
    for i in range(n):
        if s[i]==x:
            count+=i+1
            t.append(i+1)
        elif t:
            count+=t[-1]
    print(count)