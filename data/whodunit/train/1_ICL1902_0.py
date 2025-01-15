import math
def call():
    k = int(input())
    coN=0
    while(k>0):
        t = math.floor(math.sqrt(k))
        k-=t*t
        coN+=1
    print(coN)
t = int(input())
for i in range(t):
    call()