T = int(input())
for _ in range(T):
    S = input()
    codes = set()
    for i in range(len(S)-1):
        codes.add(S[i:i+2])
    print(len(codes))