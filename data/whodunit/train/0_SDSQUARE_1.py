def perfect_digit_squares(a, b):
    perfect_squares = [0, 1, 4, 9, 121, 484]
    return sum(a <= i <= b for i in perfect_squares)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(perfect_digit_squares(a, b))