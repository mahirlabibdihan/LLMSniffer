def energy_required(n, energy_levels):
    energy_levels.sort()
    energy = 0
    for i in range(1, n):
        energy += energy_levels[i-1] * energy_levels[i]
    return energy

n = int(input())
energy_levels = list(map(int, input().split()))
print(energy_required(n, energy_levels))