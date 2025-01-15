T = int(input())
pi_approximation = str(103993 / 33102)
for _ in range(T):
    K = int(input())
    if K == 0:
        print(3)
    else:
        print(pi_approximation[:K+2])