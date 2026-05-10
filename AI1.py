V = int(input("Enter no. of Vertices: "))
E = int(input("Enter no. of Edges: "))

graph={}

print("Enter vertex names:")
for i in range(V):
    vertex = input("Vertex name: ")
    graph[vertex] = []
    
print('Enter vertices of each edge')
for edge in range(E):
    u=input('1st vertex: ')
    v=input('2nd vertex: ')
    graph[u].append(v)
    graph[v].append(u)
    
visited=set()
    
def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node,' ')
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)
            
print("\nGraph: ",graph)
            
print('\n____DFS traversal____')
starting_vertex=input('Enter Starting vertex: ')
dfs(starting_vertex)