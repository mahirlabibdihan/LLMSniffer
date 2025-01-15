for _ in range(int(input())):
    card = {}
    places = {}
    tot_cost = 0
    for i in range(int(input())-1):
        entry = input().strip()
        src,dest,cost = entry.split()
        tot_cost += int(cost[:-1])
        card[src] = entry
        
        if src in places.keys():
            places[src] += 1
        else:
            places[src] = 1
        
        if dest in places.keys():
            places[dest] += 1
        else:
            places[dest] = 1
    
    for src in card.keys():
        if places[src] == 1:
            path = src
            break
        
    while path in card.keys():
        print(card[path])
        path = card[path].split()[1]
    
    print(tot_cost, end = "$")
    print()
        