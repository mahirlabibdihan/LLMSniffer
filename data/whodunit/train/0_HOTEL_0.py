T = int(input())
for _ in range(T):
    N = int(input())
    arrivals = list(map(int, input().split()))
    departures = list(map(int, input().split()))
    arrivals.sort()
    departures.sort()
    guests_in = 1
    max_guests = 1
    i = 1
    j = 0
    while i < N and j < N:
        if arrivals[i] <= departures[j]:
            guests_in += 1
            i += 1
            if guests_in > max_guests:
                max_guests = guests_in
        else:
            guests_in -= 1
            j += 1
    print(max_guests)