T = int(input())
for _ in range(T):
    S = input()
    codes = {S[i:i+2] for i in range(len(S)-1)}
    print(len(codes))