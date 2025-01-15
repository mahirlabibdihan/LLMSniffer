def calculate_net_income(T, incomes):
    slabs = [250000, 500000, 750000, 1000000, 1250000, 1500000]
    rates = [5, 10, 15, 20, 25, 30]
    for _ in range(T):
        income = incomes[_]
        tax = 0
        for i in range(6):
            if income > slabs[i]:
                tax += (income - slabs[i]) * rates[i] / 100
                income = slabs[i]
            else:
                break
        print(int(income - tax))

T = int(input())
incomes = []
for _ in range(T):
    incomes.append(int(input()))
calculate_net_income(T, incomes)