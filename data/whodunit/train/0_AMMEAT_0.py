import heapq

def min_plates(T, test_cases):
    for _ in range(T):
        N, M, P = test_cases[_]
        P = [-1*i for i in P]
        heapq.heapify(P)
        count = 0
        while M > 0 and P:
            M += heapq.heappop(P)
            count += 1
        if M > 0:
            print(-1)
        else:
            print(count)

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    test_cases.append((N, M, P))
min_plates(T, test_cases)