T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    problems = [input().strip() for _ in range(N)]
    if problems.count("cakewalk") >= 1 and problems.count("simple") >= 1 and problems.count("easy") >= 1 and (problems.count("easy-medium") >= 1 or problems.count("medium") >= 1) and (problems.count("medium-hard") >= 1 or problems.count("hard") >= 1):
        print("Yes")
    else:
        print("No")