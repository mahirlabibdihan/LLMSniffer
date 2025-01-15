from math import factorial
from collections import Counter

MOD = 10**9 + 7

def solve(word):
    freq = Counter(word)
    total = factorial(len(word))
    for letter in freq:
        total //= factorial(freq[letter])
    return total % MOD

T = int(input().strip())
for _ in range(T):
    word = input().strip()
    print(solve(word))