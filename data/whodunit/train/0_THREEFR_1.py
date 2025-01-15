T = int(input())
for _ in range(T):
    amounts = sorted(list(map(int, input().split())))
    if amounts[0] + amounts[1] == amounts[2]:
        print("yes")
    else:
        print("no")