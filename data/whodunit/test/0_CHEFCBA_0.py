def check_proportion(a, b, c, d):
    if a/b == c/d or a/c == b/d or a/d == b/c:
        return "Possible"
    else:
        return "Impossible"

a, b, c, d = map(int, input().split())
print(check_proportion(a, b, c, d))