'''
Breadth First Search is a vertex-based technique to find the shortest
path to a specific node in the graph. It uses the queue data structure
that follows the First-In-First-Out (FIFO) approach. In BFS, one vertex
is selected at a time when it is visited, then visiting the neighbouring nodes
within the same layer of the graph, in accordance to how it is stored in the
queue. In comparison to DFS, it is slower.

Time Complexity: O(V + E) or O(V^2)
'''

def breadth_first_search(graph, root_node, target_node):
    visited = []
    queue = []

    queue.append((root_node, [root_node]))

    while queue:
        node = queue.pop(0)

        if node[0] == target_node:
            return node[1]

        visited.append(node[0])
        for neighbour in graph[node[0]]:
            if neighbour not in visited:
                queue.append((neighbour, node[1] + [neighbour]))



if __name__ == '__main__':
    graph = {
    'A': ['B', 'C', 'D'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'D'], 
    'D': ['B', 'C', 'A', 'E'], 
    'E': ['B', 'D', 'F'],
    'F': ['E']
    }
    start_node = 'A'
    end_node = 'F'
    shortest_path = breadth_first_search(graph, start_node, end_node)
