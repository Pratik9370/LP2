from collections import deque 

def create_graph(): 
    graph = {}                      #Dictionary 
    n = int(input("Enter number of vertices: ")) 
    for i in range(n): 
        node = input(f"Enter vertex {i+1}: ") 
        graph[node] = [] 

    e = int(input("Enter number of edges: ")) 

    for i in range(e): 
        u = input("Enter first vertex of edge: ") 
        v = input("Enter second vertex of edge: ") 

        # Undirected graph (both directions) 
        graph[u].append(v) 
        graph[v].append(u) 

    return graph 

def dfs(graph, node, visited): 
    if node not in visited: 
        print(node, end=" ") 
        visited.add(node) 

        for neighbor in graph[node]: 
            dfs(graph, neighbor, visited) 

def bfs(graph, start): 
    visited = set() 
    queue = deque() 

    queue.append(start) 
    visited.add(start) 

    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 

        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 

# ---------------- Main Program ---------------- 
def main(): 
    graph = create_graph() 

    print("\nGraph:", graph) 

    start = input("\nEnter starting vertex: ") 

    print("\nDFS Traversal:") 
    visited = set() 
    dfs(graph, start, visited) 

    print("\n\nBFS Traversal:") 
    bfs(graph, start) 

main()
