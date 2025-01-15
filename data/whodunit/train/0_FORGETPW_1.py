T = int(input())
for _ in range(T):
    N = int(input())
    rules = {input().split()[0]: input().split()[1] for _ in range(N)}
    S = input()
    password = "".join([rules.get(char, char) for char in S])
    password = password.lstrip('0')
    if '.' in password:
        password = password.rstrip('0').rstrip('.')
    print(password)