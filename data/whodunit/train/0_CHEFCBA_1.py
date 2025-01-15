def check_proportion(a, b, c, d):
    numbers = [a, b, c, d]
    numbers.sort()
    if numbers[0]/numbers[1] == numbers[2]/numbers[3]:
        return "Possible"
    else:
        return "Impossible"

a, b, c, d = map(int, input().split())
print(check_proportion(a, b, c, d))