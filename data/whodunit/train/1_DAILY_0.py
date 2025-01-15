import math
X,N=map(int,input().split())
empty_spaces=0
for i in range(N):
    car=list(map(int,input()))
    car.insert(0,-1)
    for j in range(9):
        empty_in_comp=0
        for k in range(1,5):
            if(car[j*4+k]==0):
                empty_in_comp+=1
        for k in range(2):
            if(car[54-2*j-k]==0):
                empty_in_comp+=1
        if(empty_in_comp>=X):
            empty_spaces+=math.factorial(empty_in_comp)/math.factorial(empty_in_comp-X)/math.factorial(X)
print(int(empty_spaces))