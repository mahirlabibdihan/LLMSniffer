T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    minSalary = list(map(int, input().split()))
    offeredSalary = []
    maxJobOffers = []
    for _ in range(M):
        x, y = map(int, input().split())
        offeredSalary.append(x)
        maxJobOffers.append(y)
    qual = [list(map(int, list(input()))) for _ in range(N)]
    company = [0]*M
    salary = [0]*N
    job = [0]*N
    for i in range(N):
        max_salary = -1
        for j in range(M):
            if qual[i][j] and maxJobOffers[j] > 0 and offeredSalary[j] > max_salary:
                max_salary = offeredSalary[j]
                index = j
        if max_salary >= minSalary[i]:
            salary[i] = max_salary
            job[i] = 1
            maxJobOffers[index] -= 1
            company[index] = 1
    print(sum(job), sum(salary), M - sum(company))