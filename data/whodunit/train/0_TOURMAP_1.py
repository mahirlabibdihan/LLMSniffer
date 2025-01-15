T = int(input())
for _ in range(T):
    N = int(input())
    cards = {}
    cities = set()
    total_cost = 0
    for _ in range(N-1):
        A, B, C = input().split()
        C = int(C)
        cards[A] = (B, C)
        cities.add(A)
        cities.add(B)
        total_cost += C
    start = list(cities - set(cards.values()))[0]
    itinerary = [start]
    while len(itinerary) < N:
        itinerary.append(cards[itinerary[-1]][0])
    for i in range(N-1):
        print(itinerary[i], itinerary[i+1], cards[itinerary[i]][1])
    print(total_cost)