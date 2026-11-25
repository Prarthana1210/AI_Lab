import random
import math

N = 8

def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def neighbour(state):
    next_state = state.copy()

    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)

    next_state[col] = row

    return next_state


def simulated_annealing():
    current = [random.randint(0, N - 1) for _ in range(N)]

    T = 100

    while T > 0:

        current_cost = cost(current)

        if current_cost == 0:
            return current

        next_state = neighbour(current)

        next_cost = cost(next_state)

        delta_E = current_cost - next_cost

        if delta_E > 0:
            current = next_state

        else:
            p = math.exp(delta_E / T)

            r = random.random()

            if r < p:
                current = next_state

        T -= 1

    return current


solution = simulated_annealing()

print("Solution:", solution)
print("Cost:", cost(solution))

for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()