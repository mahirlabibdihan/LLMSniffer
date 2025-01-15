def calculate_net_income(T, incomes):
    for _ in range(T):
        income = incomes[_]
        if income <= 250000:
            print(income)
        elif income <= 500000:
            print(income - (income - 250000) * 0.05)
        elif income <= 750000:
            print(income - 12500 - (income - 500000) * 0.1)
        elif income <= 1000000:
            print(income - 37500 - (income - 750000) * 0.15)
        elif income <= 1250000:
            print(income - 75000 - (income - 1000000) * 0.2)
        elif income <= 1500000:
            print(income - 125000 - (income - 1250000) * 0.25)
        else:
            print(income - 187500 - (income - 1500000) * 0.3)

T = int(input())
incomes = []
for _ in range(T):
    incomes.append(int(input()))
calculate_net_income(T, incomes)