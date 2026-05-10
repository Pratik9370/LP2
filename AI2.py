from collections import deque

graph={}

V=int(input('Enter number of vertices: '))
for i in range(V):
    node=input('Enter vertex: ')
    graph[node]=[]
    
E=int(input('Enter number of edges: '))
for i in range(E):
    u=input('Enter 1st vertex: ')
    v=input('Enter 2nd vertex: ')
    graph[u].append(v)
    graph[v].append(u)

queue=deque()
visited=set()

def bfs():
    if not queue:
        return
    
    node=queue.popleft()
    if node not in visited:
        visited.add(node)
        print(node,' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    bfs()
            
start_node=input('Enter starting node: ')
queue.append(start_node)
bfs()