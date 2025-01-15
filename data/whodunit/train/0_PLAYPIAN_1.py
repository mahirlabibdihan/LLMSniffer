T = int(input())
for _ in range(T):
    s = input()
    if any(s[i] == s[i+1] for i in range(len(s)-1)):
        print('no')
    else:
        print('yes')