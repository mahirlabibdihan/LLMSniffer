def maximize_interaction(T, test_cases):
    for _ in range(T):
        N, K, A, B = test_cases[_]
        interaction = [a*b for a, b in zip(A, B)]
        min_interaction = min(interaction, key=abs)
        if min_interaction < 0 and K > 0:
            interaction[interaction.index(min_interaction)] += 2*K*min_interaction
        elif min_interaction > 0 and K > 0:
            interaction[interaction.index(min_interaction)] -= 2*K*min_interaction
        print(sum(interaction))

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    test_cases.append((N, K, A, B))
maximize_interaction(T, test_cases)