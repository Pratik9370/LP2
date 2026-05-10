import heapq

graph={}
nodes=[]
edges=[]

V=int(input('Enetr number of vertices: '))
for i in range(V):
    node=input('Enter vertex: ')
    nodes.append(node)
    graph[node]=[]
    
E=int(input('Enter numberof edges: '))
for i in range(E):
    u=input('Starting vertex: ')
    v=input('Ending vertex: ')
    w=int(input('Weight of edge: '))
    edges.append((u,v,w))
    graph[u].append((v,w))
    graph[v].append((u,w))
    
def prims_MST(start):
    visited=set()
    min_heap=[(0,start,None)]
    mst=[]
    total_cost=0
    
    while(min_heap):
        weight, node, parent = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst.append((weight,node,parent))
            total_cost+=weight
        
            for neighbour,w in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(min_heap,(w,neighbour,node))
    
    for weight,node,parent in mst:
        print(parent,'-->',node,' = ',weight)
        
    print('Cost of MST: ',total_cost)

start=input('Enter starting node: ')
prims_MST(start)


parent={}
for i in nodes:
    parent[i]=i
    
def find_root(node):
    while parent[node]!=node:
        node=parent[node]
    return node
        
def change_root(x,y):
    parent[x]=y

edges=sorted(edges, key=lambda item:item[2])

def kruskal_MST():
    mst=[]
    total_cost=0
    
    for u,v,w in edges:
        root_u=find_root(u)
        root_v=find_root(v)
        
        if root_u!=root_v:
            change_root(root_u,root_v)
            mst.append((u,v,w))
            total_cost+=w
    
    for u,v,w in mst:
        print(u,'-->',v,' = ',w)
    
    print(total_cost)
    
kruskal_MST()
    