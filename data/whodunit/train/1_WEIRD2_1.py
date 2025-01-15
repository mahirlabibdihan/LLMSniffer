T = int(input())


for i in range(T):
    count = {}
    pair = 0
    N = int(input())
    inp = input().split(' ')
    for j in range(N):
        if inp[j] in count:
            count[inp[j]] = count[inp[j]] + 1
        else:
            count[inp[j]] = 1
    for key in count.keys():
        for k in range(int(key),count[key]+1):
            #print(count[str(k)])
            if (str(k) in count) and (count[str(k)]>=int(key)):
                if int(key)==k:
                    pair = pair + 1
                else:
                    pair = pair + 2
    print(pair)