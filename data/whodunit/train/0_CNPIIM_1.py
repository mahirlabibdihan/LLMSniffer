def count_matrices(T, traces):
    for N in traces:
        print((N//2)**2 if N % 2 == 0 else ((N - 1)//2)**2)

T = int(input())
traces = [int(input()) for _ in range(T)]
count_matrices(T, traces)