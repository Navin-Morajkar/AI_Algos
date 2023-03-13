# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F', 'G'],
         'C': ['I'],
         'D': [],
         'E': [],
         'F': ['L'],
         'G': ['H'],
         'H': [],
         'K': [],
         'I': ['K', 'J'],
         'L': [],
         'J': []}


def bfs(graph, start,goal):
    explored = []
    if start in goal:
        print('root node itself is goal')
        return explored

    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node in goal:
            print('Goal Found:',node)
            print('TRAVERSAL ORDER:')
            for v in explored:
                print("-", v, "-")
            return "success"
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

goal=['G','J']
bfs(graph, 'A',goal)


