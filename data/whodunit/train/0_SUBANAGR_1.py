def find_longest_string(n, strings):
    common_letters = set(strings[0])
    for s in strings[1:]:
        common_letters &= set(s)
    if not common_letters:
        return 'no such string'
    counts = [min(s.count(c) for s in strings) for c in common_letters]
    result = ''.join([c * v for c, v in zip(common_letters, counts)])
    return ''.join(sorted(result))

n = int(input().strip())
strings = [input().strip() for _ in range(n)]
print(find_longest_string(n, strings))