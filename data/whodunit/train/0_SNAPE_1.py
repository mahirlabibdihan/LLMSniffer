import math
T = int(input())
for _ in range(T):
    B, LS = map(int, input().split())
    min_RS = (LS**2 - B**2)**0.5
    max_RS = (LS**2 + B**2)**0.5
    print(min_RS, max_RS)