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
    



jobs=[]

J=int(input('Enter number of jobs: '))
for i in range(J):
    id=input(f'Enter id for job {i+1}: ')
    deadline=int(input(f'deadline of {id}: '))
    profit=int(input(f'profit of {id}: '))
    jobs.append((id,deadline,profit))
    
jobs.sort(key=lambda item:item[2], reverse=True)

max_deadline=max(job[1] for job in jobs)

slots=[False]*(max_deadline+1)
selected_jobs=[]
total_profit=0

for id,deadline,profit in jobs:
    for slot in range(deadline,0,-1):
        if slots[slot]==False:
            slots[slot]=True
            selected_jobs.append(id)
            total_profit+=profit
            break

print(selected_jobs,total_profit)

