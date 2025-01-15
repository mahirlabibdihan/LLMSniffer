n = int(input())
s = input()
l = list(s)
x=[]
a = 0
l.reverse()
for i in range(n):
    if(l[i]=='1'):
        a=i
        break
print(a)