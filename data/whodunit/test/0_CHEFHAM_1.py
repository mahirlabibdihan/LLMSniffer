from collections import deque

def max_hamming_distance(t, test_cases):
    for _ in range(t):
        n = test_cases[_][0]
        a = test_cases[_][1]
        b = deque(a)
        b.rotate(1)
        hamming_distance = sum([1 for i in range(n) if a[i] != b[i]])
        print(hamming_distance)
        print(' '.join(map(str, b)))

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

max_hamming_distance(t, test_cases)