def min_tickets(n, t):
    t.sort(reverse=True)
    tickets = t[0]
    for i in range(1, n):
        tickets = max(tickets-1, t[i])
    return tickets + 1

n = int(input())
t = list(map(int, input().split()))
print(min_tickets(n, t))