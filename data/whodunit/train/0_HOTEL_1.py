T = int(input())
for _ in range(T):
    N = int(input())
    arrivals = list(map(int, input().split()))
    departures = list(map(int, input().split()))
    timeline = [(t, 1) for t in arrivals] + [(t, -1) for t in departures]
    timeline.sort()
    max_guests = 0
    guests_in = 0
    for _, delta in timeline:
        guests_in += delta
        max_guests = max(max_guests, guests_in)
    print(max_guests)