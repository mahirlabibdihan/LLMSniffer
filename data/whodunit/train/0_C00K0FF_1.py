T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    problems = [input().strip() for _ in range(N)]
    difficulties = ["cakewalk", "simple", "easy", ["easy-medium", "medium"], ["medium-hard", "hard"]]
    for difficulty in difficulties:
        if isinstance(difficulty, list):
            if not any(problem in problems for problem in difficulty):
                print("No")
                break
        elif difficulty not in problems:
            print("No")
            break
    else:
        print("Yes")