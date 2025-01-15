T= int(input())
for i in range(T):
    N = int(input())
    a1 = 250000
    a2 = 250000*0.95
    a3 = 250000*0.9
    a4 = 250000*0.85
    a5 = 250000*0.8
    a6 = 250000*0.75
    
    if N<=250000:
        print(N)
    elif 250000<N<= 500000:
        print(int(0.95*(N-250000) + a1))
    elif 500000< N<=750000:
        print(int(0.9*(N-500000) + a2+a1))
    elif 750000<N<=1000000:
        print(int(0.85*(N-750000)+a3+a2+a1))
    elif 1000000<N<=1250000:
        print(int(0.8*(N-1000000)+a4+a3+a2+a1))
    elif 1250000<N<=1500000:
        print(int(0.75*(N-1250000)+a5+a4+a3+a2+a1))
    else: print(int(0.7*(N-1500000)+a6+a5+a4+a3+a2+a1))