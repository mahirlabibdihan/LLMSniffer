T = int(input())
for _ in range(T):
    N = int(input())
    rules = {}
    for _ in range(N):
        c, p = input().split()
        rules[c] = p
    S = input()
    password = ""
    for char in S:
        if char in rules:
            password += rules[char]
        else:
            password += char
    password = password.lstrip('0')
    if '.' in password:
        password = password.rstrip('0').rstrip('.')
    print(password)