import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def get_blank_position(state):
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value is None:
                return i, j

def get_manhattan_distance(i, j, goal_i, goal_j):
    return abs(i - goal_i) + abs(j - goal_j)

def generate_new_state(state, blank_i, blank_j, new_i, new_j):
    new_state = [row.copy() for row in state]
    new_state[blank_i][blank_j] = new_state[new_i][new_j]
    new_state[new_i][new_j] = None
    return new_state

def generate_children(node, goal_state):
    moves = [
        ('UP', -1, 0),
        ('DOWN', 1, 0),
        ('LEFT', 0, -1),
        ('RIGHT', 0, 1)
    ]
    blank_i, blank_j = get_blank_position(node.state)

    children = []
    for move, di, dj in moves:
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = generate_new_state(node.state, blank_i, blank_j, new_i, new_j)
            heuristic = sum(
                get_manhattan_distance(i, j, goal_i, goal_j)
                for i, row in enumerate(new_state)
                for j, value in enumerate(row)
                if value is not None
                for goal_i, goal_row in enumerate(goal_state)
                for goal_j, goal_value in enumerate(goal_row)
                if goal_value == value
            )
            child = PuzzleNode(new_state, node, move, node.cost + 1, heuristic)
            children.append(child)

    return children

def solve_8_puzzle(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state)
    goal_node = PuzzleNode(goal_state)

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            moves = []
            while current_node.move:
                moves.insert(0, current_node.move)
                current_node = current_node.parent
            return moves

        closed_set.add(tuple(map(tuple, current_node.state)))

        children = generate_children(current_node, goal_state)
        for child in children:
            if tuple(map(tuple, child.state)) in closed_set:
                continue
            heapq.heappush(open_list, child)

    return None

# Example usage
initial_state = [
    [2, 8, 3],
    [1, None, 4],
    [7, 6, 5]
]

goal_state = [
    [1, 2, 3],
    [8, None, 4],
    [7, 6, 5]
]

solution = solve_8_puzzle(initial_state, goal_state)
if solution:
    print("Solution found! Moves:", solution)
else:
    print("no solution")
