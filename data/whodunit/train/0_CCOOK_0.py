N = int(input())
for _ in range(N):
    problems_solved = sum(map(int, input().split()))
    if problems_solved == 0:
        print("Beginner")
    elif problems_solved == 1:
        print("Junior Developer")
    elif problems_solved == 2:
        print("Middle Developer")
    elif problems_solved == 3:
        print("Senior Developer")
    elif problems_solved == 4:
        print("Hacker")
    else:
        print("Jeff Dean")