steps = {
    "T": 2,
    "S": 1
}

octave = 12             # 12 keys per octave

def length(phrase):
    return sum([steps[s] for s in phrase])

# Each phrase produces X results, where
#
# X = max((total keys available - length of phrase) + 1, 0)
#
# Keep repeating the phrase and recalculating X until X < 0
def results(keys, l):
    return keys - l

for t in range(int(input())):
    s = str(input())
    n = int(input())
    ans = 0
    repeat = 1
    number_of_keys = octave * n
    r = results(number_of_keys, length(s * repeat))
    while r >= 0:
        ans += r
        repeat += 1
        r = results(number_of_keys, length(s * repeat))
    print(ans)
