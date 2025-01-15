def solve(s, t):
    freq = [0]*26
    for i in s:
        freq[ord(i)-97] += 1
    for i in t:
        freq[ord(i)-97] += 1
    for i in range(25, -1, -1):
        if freq[i]%2:
            return 'A' if s.count(chr(i+97))%2 else 'B'
    return 'B'

T = int(input())
for _ in range(T):
    s = input()
    t = input()
    print(solve(s, t))