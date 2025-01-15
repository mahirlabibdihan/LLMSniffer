def min_tickets(n, t):
    t.sort()
    tickets = t[-1]
    for i in range(n-2, -1, -1):
        tickets = max(tickets-1, t[i])
    return tickets + 1

n = int(input())
t = list(map(int, input().split()))
print(min_tickets(n, t))