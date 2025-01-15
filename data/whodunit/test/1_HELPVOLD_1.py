# # # t=int(input())
# # # for i in range(t):
# # #     n=int(input())
# # #     a=[]
# # #     b=[]
# # #     for j in range(n):
# # #         x,y =map(int,input().split())
# # #         a.append(x)
# # #         b.append(y)
# # #     print(len(set(a))+len(set(b)))
# # t=int(input())
# # for i in range(t):
# #     n=int(input())
# #     N=list(map(int,input().split()))
# #     x=float(sum(N)/n)
# #     if x>=4 and min(N)>2 and 5 in N:
# #         print("YES")
# #     else:
# #         print("NO")

# t =int(input())
# for i in range(t):
#     s=input()
#     l=s.split(' ')
#     if len(l)==1:
#         print(s.casefold().capitalize())
#     elif len(l)==2:
#         print(l[0][0].capitalize()+'. '+l[1].casefold().capitalize())
#     else:
#         print(l[0][0].capitalize()+'. '+l[1][0].capitalize()+'. '+l[2].casefold().capitalize())
# t=int(input())
# for i in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     l.sort()
#     a,b=l[0],l[len(l)-1]
#     d=0
#     for j in range(1,len(l)-1):
#         if (b-l[j])+(l[j]-a) >d:
#             d=(b-l[j])+(l[j]-a)
#     print(d+b-a)
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans =0
for j in range(len(l)-1):
    ans = ans +l[j]*l[j+1]
print(ans)