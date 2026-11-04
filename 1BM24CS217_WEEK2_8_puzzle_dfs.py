# 8-Puzzle using Depth First Search (DFS)

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Display the puzzle
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Generate possible moves
def get_neighbors(state):
    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        # Check whether move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors


# DFS function
def dfs(state, path, visited):

    # Goal test
    if state == GOAL:
        return path

    # Mark current state as visited
    visited.add(state)

    # Generate next states
    for new_state, move in get_neighbors(state):

        if new_state not in visited:

            result = dfs(
                new_state,
                path + [move],
                visited
            )

            if result is not None:
                return result

    return None


# Initial state
initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)


print("Initial State:")
print_state(initial)

print("Goal State:")
print_state(GOAL)


# Start DFS
visited = set()

solution = dfs(initial, [], visited)


# Display result
if solution is not None:
    print("Solution:")
    print(" -> ".join(solution))

    print("Number of moves:", len(solution))
else:
    print("No solution found.")