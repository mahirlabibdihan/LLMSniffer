N = int(input())
classification = ["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"]
for _ in range(N):
    problems_solved = sum(map(int, input().split()))
    print(classification[problems_solved])