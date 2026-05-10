arr=[12,5,4,1,6,9]

for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)



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