def s(t):
    a=0
    for k in str(t):
        a+=int(k)
    return a
def ss(t):
    a=0
    for k in str(s(t)):
        a+=int(k)
    return a

n=int(input())
c=0
for i in range(n-9*len(str(n))-9*(len(str(9*len(str(n))))),n+9*len(str(n))+9*(len(str(9*len(str(n)))))+1):
    if i+s(i)+ss(i)==n:
        #print(i,'+',s(i),'+',ss(i))
        c+=1
print(c)