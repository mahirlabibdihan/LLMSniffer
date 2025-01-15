T = int(input().strip())
for _ in range(T):
    S = input().strip()
    count = sum(S[i] == S[i+1] for i in range(len(S)-1))
    print(count)