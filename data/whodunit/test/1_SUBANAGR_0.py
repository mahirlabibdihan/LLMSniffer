n=int(input())
a=[[0]*26]*n
m=[1000000000]*26
for i in range(n):
    a[i]=input()
for i in range(26):
    for j in range(n):
        x=chr(97+i)
        m[i]=min(a[j].count(chr(97+i)),m[i])
ans=""
for i in range(26):
    ans+=m[i]*chr(ord('a')+i)
if(len(ans)):
    print(ans)
else:
    print('no such string')