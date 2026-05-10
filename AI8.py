import heapq


V=int(input('Enter number of Vertex: '))
nodes=[]
for i in range(V):
    node=input('Enter vertex: ')
    nodes.append(node)
parent={}
for node in nodes:
    parent[node]=node

E=int(input('Enter number of Edges: '))
edges=[]
for i in range(E):
    u=input('Starting vertex: ')
    v=input('Ending vertex: ')
    w=int(input('Weight of edge: '))
    edges.append((u,v,w))

edges=sorted(edges, key=lambda item:item[2])

def find_parent(node):
    while parent[node]!=node:
        node=parent[node]
    return node

def change_parent(x,y):
    parent[x]=y
    
MST=[]

def Kruskal_MST():
    Weight=0
    for u,v,w in edges:
        root_u=find_parent(u)
        root_v=find_parent(v)
        if root_u!=root_v:
            MST.append((u,v,w))
            change_parent(root_u,root_v)
            Weight+=w
            
    for u,v,w in MST:
        print(u,'-->',v,' = ',w)

    print('Total Weight of MST is: ',Weight)
    
Kruskal_MST()



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
    
