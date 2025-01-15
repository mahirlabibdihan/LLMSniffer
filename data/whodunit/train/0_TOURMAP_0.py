T = int(input())
for _ in range(T):
    N = int(input())
    cards = []
    cities = set()
    total_cost = 0
    for _ in range(N-1):
        A, B, C = input().split()
        C = int(C)
        cards.append((A, B, C))
        cities.add(A)
        cities.add(B)
        total_cost += C
    start = [card[0] for card in cards if card[0] not in [card[1] for card in cards]][0]
    itinerary = [start]
    while len(itinerary) < N:
        for card in cards:
            if card[0] == itinerary[-1]:
                itinerary.append(card[1])
                break
    for i in range(N-1):
        print(itinerary[i], itinerary[i+1], [card[2] for card in cards if card[0] == itinerary[i] and card[1] == itinerary[i+1]][0])
    print(total_cost)