T = int(input())
for _ in range(T):
    s = list(input())
    l = len(s)
    possible = True
    for i in range(l//2):
        if s[i] != '.' and s[l-i-1] != '.' and s[i] != s[l-i-1]:
            possible = False
            break
        elif s[i] == '.' and s[l-i-1] != '.':
            s[i] = s[l-i-1]
        elif s[i] != '.' and s[l-i-1] == '.':
            s[l-i-1] = s[i]
        elif s[i] == '.' and s[l-i-1] == '.':
            s[i] = s[l-i-1] = 'a'
    if l % 2 != 0 and s[l//2] == '.':
        s[l//2] = 'a'
    print(''.join(s) if possible else -1)