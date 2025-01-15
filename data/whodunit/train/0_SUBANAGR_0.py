from collections import Counter

def find_longest_string(n, strings):
    counts = [Counter(s) for s in strings]
    common_counts = counts[0]
    for count in counts[1:]:
        common_counts &= count
    result = ''.join([chr(ord('a') + i) * v for i, v in enumerate(common_counts.elements())])
    return result if result else 'no such string'

n = int(input().strip())
strings = [input().strip() for _ in range(n)]
print(find_longest_string(n, strings))