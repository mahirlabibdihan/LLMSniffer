def is_beautiful(s):
    s += s[0]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return "no"
    return "yes"

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(is_beautiful(s))