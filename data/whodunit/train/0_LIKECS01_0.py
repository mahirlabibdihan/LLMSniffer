def find_subsequence(T, strings):
    for _ in range(T):
        S = strings[_]
        if len(S) != len(set(S)):
            print("yes")
        else:
            print("no")

T = int(input())
strings = []
for _ in range(T):
    strings.append(input())
find_subsequence(T, strings)