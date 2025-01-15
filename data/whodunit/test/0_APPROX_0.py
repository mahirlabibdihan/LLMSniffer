T = int(input())
for _ in range(T):
    K = int(input())
    if K == 0:
        print(3)
    else:
        print("3." + str(103993//33102)[1:K+1])