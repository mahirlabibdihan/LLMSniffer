N, r = map(int, input().split())
ratings = [int(input()) for _ in range(N)]
for rating in ratings:
    print("Good boi" if rating >= r else "Bad boi")