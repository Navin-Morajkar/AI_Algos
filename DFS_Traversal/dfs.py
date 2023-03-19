# Enter number of nodes in the graph
num_of_nodes = int(input("Enter the total number of nodes: "))

# Create an empty dictionary to represent the graph
graph = {}

# Loop through each node & ask for its children
for i in range(num_of_nodes):
    node = input(f"\nEnter the name of node {i+1}: ")
    children = input(f"Enter the children of node {node}: ").split()
    graph[node] = children

print("\nThe graph is: ")
print(graph)


# DFS function
def dfs(graph, start, goal):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node in goal:
            print("Goal Found: ", node)
            visited.insert(0, node)
            visited.reverse()
            print("Traversal Order: ", visited)
            return "Success"

        if node not in visited:
            visited.insert(0, node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.insert(0, neighbor)

    print("Goal Not Found")
    visited.reverse()
    print("Traversal Order:", visited)
    return visited

# Function calls with diff i/p
zero_goal = []
print("\nZero Goal Nodes case: ")
dfs(graph, 'A', zero_goal)

print("\nSingle Goal Node case: ")
single_goal = input("Enter node for single goal node case: ")
print("Your single goal node list has the node: ", single_goal)
dfs(graph, 'A', single_goal)

print("\nMultiple Goal Nodes case: ")
multi_goal = input("Enter nodes for multiple goal node case: ").split()
print("The multiple goal nodes are ", multi_goal)
dfs(graph, 'A', multi_goal)