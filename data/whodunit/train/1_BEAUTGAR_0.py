def solve():
    s = input()
    rs, gs = s.count('R'), s.count('G')
    if rs != gs:
        return 'no'

    count_g, count_r = 0, 0

    if s[0] == s[len(s)-1]:
        if s[0] == 'R':
            count_r += 1
        else:
            count_g += 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            if s[0] == 'R':
                count_r += 1
            else:
                count_g += 1

    if count_g+count_r == 2 or count_r+count_g == 0:
        return 'yes'
    else:
        return 'no'


tc = int(input())
for _ in range(tc):
    print(solve())
