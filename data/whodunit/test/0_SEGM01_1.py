T = int(input().strip())
for _ in range(T):
    S = input().strip()
    ones = S.count('1')
    segment = S[S.find('1'):S.rfind('1')+1]
    if segment.count('1') == ones:
        print("YES")
    else:
        print("NO")