T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd = len([a for a in A if a % 2 == 1])
    even = len([a for a in A if a % 2 == 0])
    print(odd * even)