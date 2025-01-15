T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    S = input()
    X = [int(i) for i in input().split()]

    i = 0
    # j = 0
    total = 0
    temp = 0
    while(i<N):
        if(S[i]=='1'):
            j = i+1
            maxd = -float('inf')
            while(j<N and S[j]=='0'):
                temp += X[j]-X[j-1]
                if(X[j]-X[j-1]>maxd):
                    maxd = X[j]-X[j-1]
                j += 1
            if(j<N and S[j]=='1'):
                temp += X[j]-X[j-1]
                if(X[j]-X[j-1]>maxd):
                    maxd = X[j]-X[j-1]
                temp -= maxd
                total += temp
                temp = 0
            i = j
        else:
            i += 1
    # correction = 0
    # if(S[0]!='1'):
    #     for i in range(1,N):
    #         correction += X[i]-X[i-1]
    #         if(S[i]=='1'):
    #             break
    correction = 0
    for i in range(N-1):
        if(S[i]=='1'):
            break
        correction += X[i+1]-X[i]
    total += temp + correction
    ans.append(total)

for i in ans:
    print(i)
