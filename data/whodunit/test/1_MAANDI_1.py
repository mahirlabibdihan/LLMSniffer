def divisors(n):
    r = []
    a = int(n**(0.5)+1)
    for i in range(1,a):
        if n%i==0:
            r.append(i)
            if n//i!=i:
                r.append(n//i)
    return r
def lucky(n):
    for i in n:
        if i!='4' or i!='7':
            return False
    return True
def overlucky(n):
    s = ''
    for i in n:
        if i=='4' or i=='7':
            s+=i
    if s=='':
        return False
    else:
        return True
T = int(input())
for i in range(T):
    N = int(input())
    count=0
    for i in divisors(N):
        if lucky(str(i)):
            count+=1
        else:
            if overlucky(str(i)):
                count+=1
    print(count)            
    