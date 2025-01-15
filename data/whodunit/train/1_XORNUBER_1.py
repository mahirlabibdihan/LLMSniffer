from sys import *
test = int(input())
for tt in range(test):
    n = int(input())
    t = -1
    for i in range(30):
        if(n == 2**i-1):
            t = i
            break
    if (t == 1):
        print(2)
    elif(t == -1):
        print(-1)
    else:
        print(2**(t-1) -1)

