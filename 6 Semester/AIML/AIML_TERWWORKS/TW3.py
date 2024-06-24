#TW 3

import heapq

def astar(graph, start, goal, heuristic):
    # Priority queue for nodes to be explored
    queue = [(0 + heuristic[start], start, [])]  # (priority, node, path)
    # Cost to reach each node from start
    cost_so_far = {start: 0}
    # Counter for iteration step
    iteration_step = 0

    while queue:
        iteration_step += 1
        # Get the node to explore next
        _, current, path = heapq.heappop(queue)

        print("Iteration", iteration_step, "- Current node:", current, "- Path:", path)

        # Goal reached, return the path
        if current == goal:
            return path + [current], iteration_step

        # Explore neighbors
        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            # Update cost if the new path is cheaper or this is the first time visiting the node
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (priority, neighbor, path + [current]))
                print("   -> Neighbor:", neighbor, "- Path:", path + [current], "- Cost:", new_cost, "- Priority:", priority)

    # No path found
    return None, iteration_step

# Example graph represented as an adjacency list with costs
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 4},
    'C': {'F': 2},
    'D': {},
    'E': {'G': 5},
    'F': {},
    'G': {}
}

# Heuristic values for each node
heuristic = {
    'A': 10,
    'B': 5,
    'C': 8,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

# Perform A* search
path, iterations = astar(graph, start_node, goal_node, heuristic)

# Print the result
if path:
    print("Path found:", path)
    total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
    print("Total cost:", total_cost)
else:
    print("No path found.")

print("Iterations:", iterations)
