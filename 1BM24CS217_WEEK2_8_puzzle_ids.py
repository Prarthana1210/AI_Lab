GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)




def print_state(state):
    """Print the puzzle state."""
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    """Generate all possible next states."""

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

     
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

           
            new_state = list(state)

          
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors


def depth_limited_search(state, depth, path, visited):

  
    if state == GOAL:
        return path

   
    if depth == 0:
        return None

  
    for new_state, move in get_neighbors(state):

       
        if new_state not in visited:

            visited.add(new_state)

            result = depth_limited_search(
                new_state,
                depth - 1,
                path + [move],
                visited
            )

            if result is not None:
                return result

            visited.remove(new_state)

    return None


def iterative_deepening_search(initial):

    depth = 0

    while True:

        print("Searching with depth limit:", depth)

        visited = {initial}

        result = depth_limited_search(
            initial,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

        depth += 1


initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

print("Initial State:")
print_state(initial)

print("Goal State:")
print_state(GOAL)

solution = iterative_deepening_search(initial)

print("Solution:")
print(" -> ".join(solution))

print("Number of moves:", len(solution))