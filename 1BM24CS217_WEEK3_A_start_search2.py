def manhattan_distance(state, goal):
    distance = 0

    for i in range(9):
        if state[i] == 0:       
            continue

    
        current_row = i // 3
        current_col = i % 3

    
        goal_index = goal.index(state[i])
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        
        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance



state = [
    2, 8, 3,
    1, 6, 4,
    0, 7, 5
]

goal = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]

h = manhattan_distance(state, goal)

print("Manhattan Distance =", h)