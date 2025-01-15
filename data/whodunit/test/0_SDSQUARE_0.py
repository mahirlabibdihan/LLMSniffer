def perfect_digit_squares(a, b):
    perfect_squares = [0, 1, 4, 9, 121, 484]
    count = 0
    for i in perfect_squares:
        if a <= i <= b:
            count += 1
    return count

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(perfect_digit_squares(a, b))