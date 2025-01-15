def count_matrices(T, traces):
    for N in traces:
        if N % 2 == 0:
            print((N//2 - 1)**2)
        else:
            print(((N - 1)//2)**2)

T = int(input())
traces = [int(input()) for _ in range(T)]
count_matrices(T, traces)