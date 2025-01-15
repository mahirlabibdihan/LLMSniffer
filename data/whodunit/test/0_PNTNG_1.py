def min_cost_painting(N, M, H, layers):
    layers = sorted(layers, key=lambda x: x[1])
    total_cells = N * M
    total_cost = 0
    for Tk, Ck in layers:
        if total_cells <= Tk:
            total_cost += total_cells * Ck
            return total_cost
        else:
            total_cells -= Tk
            total_cost += Tk * Ck
    return "Impossible"

N, M, H = map(int, input().split())
layers = [tuple(map(int, input().split())) for _ in range(H)]
print(min_cost_painting(N, M, H, layers))