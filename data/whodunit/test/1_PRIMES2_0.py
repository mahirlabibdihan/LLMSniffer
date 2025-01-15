from math import sqrt
def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
l=[]
for i in range(2,1000):
    z=is_prime(i)
    if z==True:
        l.append(i)
ba=[]
while True:
    c=int(input())
    if c!=0:
     ba.append(c)
    else:
        break
for m in ba:
  flg=0
  for i in l:
     for j in l:
        k=m-(i**2+j**3)
        if k>1:
            if is_prime(k)==True:
                print(k,i,j)
                flg=1
                break
     if flg==1:
        break
  if flg==0:
      print(0,0,0)