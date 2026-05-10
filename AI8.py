import heapq

graph={}
nodes=[]
edges=[]

distances={}
visited=set()
min_heap=[]

V=int(input('Enter number of vertices: '))
for i in range(V):
    node=input('Enter vertex: ')
    nodes.append(node)
    graph[node]=[]
    distances[node]=float('inf')

E=int(input('Enter number of edges: '))
for i in range(E):
    u=input('Enter starting vertex: ')
    v=input('Enter ending vertex: ')
    w=int(input('Weight of edge: '))
    edges.append((u,v,w))
    graph[u].append((v,w))
    graph[v].append((u,w))

start=input('Enter starting vertex: ')
distances[start]=0

heapq.heappush(min_heap,(0,start))

while min_heap:
    current_distance,node=heapq.heappop(min_heap)
    
    if current_distance > distances[node]:
        continue
    
    for neighbour, weight in graph[node]:
        new_distance=current_distance+weight
        if new_distance<distances[neighbour]:
            distances[neighbour]=new_distance
            heapq.heappush(min_heap,(new_distance,neighbour))
            
            
for i in distances:
    print(i,' = ',distances[i])
    
