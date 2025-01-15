T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    minSalary = list(map(int, input().strip().split()))
    offeredSalary = []
    maxJobOffers = []
    for _ in range(M):
        o, m = map(int, input().strip().split())
        offeredSalary.append(o)
        maxJobOffers.append(m)
    qual = []
    for _ in range(N):
        qual.append(list(map(int, list(input().strip()))))
    company = [0]*M
    student = [0]*N
    total = 0
    for i in range(N):
        max_salary = -1
        max_index = -1
        for j in range(M):
            if qual[i][j] == 1 and maxJobOffers[j] > 0 and offeredSalary[j] > max_salary:
                max_salary = offeredSalary[j]
                max_index = j
        if max_index != -1 and max_salary >= minSalary[i]:
            maxJobOffers[max_index] -= 1
            company[max_index] = 1
            student[i] = 1
            total += max_salary
    print(sum(student), total, M - sum(company))
