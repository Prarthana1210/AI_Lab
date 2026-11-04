import heapq

def misplaced_tiles(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count



def get_neighbors(state):
    neighbors = []

    zero_index = state.index(0)

    row = zero_index // 3
    col = zero_index % 3

    
    if row > 0:
        new_state = list(state)
        swap_index = zero_index - 3
        new_state[zero_index], new_state[swap_index] = \
            new_state[swap_index], new_state[zero_index]
        neighbors.append(tuple(new_state))

    if row < 2:
        new_state = list(state)
        swap_index = zero_index + 3
        new_state[zero_index], new_state[swap_index] = \
            new_state[swap_index], new_state[zero_index]
        neighbors.append(tuple(new_state))


    if col > 0:
        new_state = list(state)
        swap_index = zero_index - 1
        new_state[zero_index], new_state[swap_index] = \
            new_state[swap_index], new_state[zero_index]
        neighbors.append(tuple(new_state))

    
    if col < 2:
        new_state = list(state)
        swap_index = zero_index + 1
        new_state[zero_index], new_state[swap_index] = \
            new_state[swap_index], new_state[zero_index]
        neighbors.append(tuple(new_state))

    return neighbors




def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def a_star(initial, goal):

    # Priority queue
    # (f, g, state, path)
    open_list = []

    h = misplaced_tiles(initial, goal)
    g = 0
    f = g + h

    heapq.heappush(open_list, (f, g, initial, [initial]))

    visited = set()

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        # Goal test
        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        # Generate successors
        for neighbor in get_neighbors(current):

            if neighbor in visited:
                continue

            new_g = g + 1
            new_h = misplaced_tiles(neighbor, goal)
            new_f = new_g + new_h

            new_path = path + [neighbor]

            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor, new_path)
            )

    return None


initial = (
    2, 8, 3,
    1, 6, 4,
    0, 7, 5
)

goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

solution = a_star(initial, goal)

if solution:

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):

        print("Step:", step)
        print_state(state)

else:
    print("No solution found.")