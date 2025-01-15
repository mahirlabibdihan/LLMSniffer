def getInput():
    arr = list(map(int,input().split()))
    if len(arr) ==1:
        return arr[0]
    return arr

for tc in range(int(input())):
    n = getInput()
    kmap = {}
    winner = "Nobody wins."
    winnum = 9999999999
    for i in range(n):
        name,num = input().split()
        num = int(num)
        if num not in kmap:
            kmap[num] = [1,name]
        else:
            kmap[num] = [kmap[num][0] + 1,name]
    for num in kmap:
        if kmap[num][0] == 1 and num<winnum:
            winnum = num
            winner = kmap[num][1]
    print(winner)
            