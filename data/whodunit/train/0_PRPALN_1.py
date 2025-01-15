def can_form_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            one, two = s[i:j], s[i + 1:j + 1]
            return "YES" if one == one[::-1] or two == two[::-1] else "NO"
        i, j = i + 1, j - 1
    return "YES"

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(can_form_palindrome(s))