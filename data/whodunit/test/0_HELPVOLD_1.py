def energy_required(n, energy_levels):
    energy_levels.sort()
    energy = 0
    for i in range(n-1):
        energy += energy_levels[i] * energy_levels[i+1]
    return energy

n = int(input())
energy_levels = list(map(int, input().split()))
print(energy_required(n, energy_levels))