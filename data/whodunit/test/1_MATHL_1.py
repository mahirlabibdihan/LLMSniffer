n=int(input())
l=[1,2,12]
A=6
a=4;
for i in range(4,1000001):
   l.append((A)%1000000007 *(a)%1000000007 * (l[len(l)-1])%1000000007)
   A=(A*a)%1000000007;
   a+=1;
for i in range(0,n):
    o=int(input())
    print(l[o-1])