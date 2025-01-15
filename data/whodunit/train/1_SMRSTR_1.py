import numpy
for _ in range(int(input())):
    n,q=map(int,input().split())
    d=[int(i) for i in input().split()]
    x=[int(j) for j in input().split()]
    result=numpy.prod(d)
    for i in range(q):
        print(x[i]//result,end=' ')