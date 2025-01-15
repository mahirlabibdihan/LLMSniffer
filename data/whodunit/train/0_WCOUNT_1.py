from math import factorial
from collections import Counter

MOD = 10**9 + 7

def solve(word):
    freq = Counter(word)
    total = 1
    for letter in freq:
        total = (total * factorial(freq[letter])) % MOD
    return (factorial(len(word)) // total) % MOD

T = int(input().strip())
for _ in range(T):
    word = input().strip()
    print(solve(word))