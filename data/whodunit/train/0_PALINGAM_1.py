def solve(s, t):
    freq = [0]*26
    for i in s:
        freq[ord(i)-97] += 1
    for i in t:
        freq[ord(i)-97] += 1
    odd_count = sum(i%2 for i in freq)
    if odd_count == 0 or odd_count%2 == 1:
        return 'A'
    else:
        return 'B'

T = int(input())
for _ in range(T):
    s = input()
    t = input()
    print(solve(s, t))