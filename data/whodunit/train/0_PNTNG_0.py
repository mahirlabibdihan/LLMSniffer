def min_cost_painting(N, M, H, layers):
    layers.sort(key=lambda x: x[1])
    total_cells = N * M
    total_cost = 0
    for i in range(H):
        if total_cells <= layers[i][0]:
            total_cost += total_cells * layers[i][1]
            return total_cost
        else:
            total_cells -= layers[i][0]
            total_cost += layers[i][0] * layers[i][1]
    return "Impossible"

N, M, H = map(int, input().split())
layers = []
for _ in range(H):
    Tk, Ck = map(int, input().split())
    layers.append((Tk, Ck))
print(min_cost_painting(N, M, H, layers))