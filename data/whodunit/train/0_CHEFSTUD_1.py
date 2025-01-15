def count_pairs(s):
    return s.count('<>')

T = int(input())
for _ in range(T):
    s = input()
    print(count_pairs(s))