import heapq 

def prim(graph, start): 
    visited = set() 
    min_heap = [(0, start, None)]   # (weight, node, parent)
    total_cost = 0 
    mst = [] 

    while min_heap: 
        weight, node, parent = heapq.heappop(min_heap) 

        if node not in visited: 
            visited.add(node) 
            total_cost += weight 

            if parent is not None:
                mst.append((parent, node, weight)) 

            for neighbor, w in graph[node]: 
                if neighbor not in visited: 
                    heapq.heappush(min_heap, (w, neighbor, node)) 

    return mst, total_cost 


def find(parent, node):
    if parent[node] != node: 
        parent[node] = find(parent, parent[node]) 
    return parent[node] 


def union(parent, rank, u, v): 
    root_u = find(parent, u) 
    root_v = find(parent, v)  

    if root_u != root_v: 
        if rank[root_u] > rank[root_v]: 
            parent[root_v] = root_u 
        elif rank[root_u] < rank[root_v]: 
            parent[root_u] = root_v 
        else: 
            parent[root_v] = root_u 
            rank[root_u] += 1 


def kruskal(nodes, edges): 
    parent = {} 
    rank = {} 

    for node in nodes: 
        parent[node] = node 
        rank[node] = 0 

    edges.sort(key=lambda x: x[2]) 

    mst = [] 
    total_cost = 0 

    for u, v, w in edges: 
        if find(parent, u) != find(parent, v): 
            union(parent, rank, u, v) 
            mst.append((u, v, w)) 
            total_cost += w 

    return mst, total_cost 


# ---------------- Main Program ---------------- 

n = int(input("Enter number of nodes: ")) 
print("Enter node names (space separated):") 
nodes = input().split() 

graph = {node: [] for node in nodes}
edges = [] 

e = int(input("Enter number of edges: ")) 
print("Enter edges (source destination weight):") 

for _ in range(e): 
    u, v, w = input().split() 
    w = int(w) 

    graph[u].append((v, w)) 
    graph[v].append((u, w)) 

    edges.append((u, v, w)) 

start = input("Enter starting node (for Prim): ") 

# Prim's Algorithm
prim_mst, prim_cost = prim(graph, start) 
print("\n--- Prim's Algorithm ---") 
print("Edges in MST:") 
for edge in prim_mst: 
    print(edge) 
print("Total Cost:", prim_cost) 

# Kruskal's Algorithm
kruskal_mst, kruskal_cost = kruskal(nodes, edges) 
print("\n--- Kruskal's Algorithm ---") 
print("Edges in MST:") 
for edge in kruskal_mst: 
    print(edge) 
print("Total Cost:", kruskal_cost)