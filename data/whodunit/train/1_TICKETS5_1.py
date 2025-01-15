def luck(S):
    if S[0] == S[1]:
        return "NO"
    for i in range(2,len(S)):
        if S[i] != S[i-2]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    S = input()
    print(luck(S))