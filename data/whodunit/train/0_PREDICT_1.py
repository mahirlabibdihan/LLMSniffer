def calculate_expected_amount(T, probabilities):
    results = []
    for PA in probabilities:
        PB = 1 - PA
        if PA > PB:
            results.append(10000 * (1 + (2 * PB)))
        else:
            results.append(10000 * (1 + (2 * PA)))
    return results

T = int(input())
probabilities = [float(input()) for _ in range(T)]
print("\n".join(map(str, calculate_expected_amount(T, probabilities))))