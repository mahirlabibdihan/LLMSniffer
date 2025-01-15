def solution():
    N, M = map(int, input().split())
    
    minSalary = list(map(int, input().split()))
    offeredSalary = []
    maxJobOffers = []
    
    for i in range(M):
        salary, offer = map(int, input().split())
        offeredSalary.append(salary)
        maxJobOffers.append(offer)
    
    qual = []

    for i in range(N):
        qual.append([ c == '1' for i, c in enumerate(input())])

    placements_count = 0
    total_salary = 0
    
    hiring_companies = set()

    for i in range(N):
        selected = -1;
        for j in range(M):
            if qual[i][j] and maxJobOffers[j] > 0 and offeredSalary[j] >= minSalary[i]:
                if selected == -1 or offeredSalary[selected] < offeredSalary[j]:
                    selected = j;
        if selected >= 0:
            maxJobOffers[selected] -= 1
            placements_count += 1
            total_salary += offeredSalary[selected]
            hiring_companies.add(selected)
    
    print(placements_count, end = " ")
    print(total_salary, end = " ")
    print(M - len(hiring_companies))


T = int(input())
while(T > 0):
    T = T - 1
    solution()
