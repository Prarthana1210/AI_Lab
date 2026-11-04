import random

N = int(input("Enter the number of queens: "))


def calculate_cost(board):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                cost += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


def get_neighbors(board):
    neighbors = []

    for row in range(N):
        for col in range(N):
            if col != board[row]:
                new_board = board.copy()
                new_board[row] = col
                neighbors.append(new_board)

    return neighbors


def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current_cost = calculate_cost(board)

        print("Current State:", board, "Cost:", current_cost)

        if current_cost == 0:
            return board

        neighbors = get_neighbors(board)

        best_neighbor = min(neighbors, key=calculate_cost)
        best_cost = calculate_cost(best_neighbor)

        if best_cost >= current_cost:
            print("Local maximum reached. Restarting...")
            board = [random.randint(0, N - 1) for _ in range(N)]
        else:
            board = best_neighbor


solution = hill_climbing()

print("\nFinal Solution:", solution)
print("Final Cost:", calculate_cost(solution))