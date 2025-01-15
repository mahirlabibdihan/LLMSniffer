def is_beautiful(s):
    return "no" if any(s[i] == s[i + 1] for i in range(len(s) - 1)) else "yes"

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    s += s[0]
    print(is_beautiful(s))