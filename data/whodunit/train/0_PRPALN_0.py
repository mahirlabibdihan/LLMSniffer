def is_palindrome(s):
    return s == s[::-1]

def can_form_palindrome(s):
    if is_palindrome(s):
        return "YES"
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if is_palindrome(t):
            return "YES"
    return "NO"

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(can_form_palindrome(s))