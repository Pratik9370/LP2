import heapq 

def heuristic(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def astar(grid, start, goal): 
    rows = len(grid) 
    cols = len(grid[0]) 

    open_list = [] 
    heapq.heappush(open_list, (0, start)) 

    came_from = {}            #Stores path
    g_score = {start: 0}          # Cost from start to node
    closed_set = set()               #Visited Nodes

    while open_list: 
        current = heapq.heappop(open_list)[1] 

        if current in closed_set:
            continue                    # Avoid Reprocessing same node

        if current == goal: 
            path = [] 
            while current in came_from: 
                path.append(current) 
                current = came_from[current] 
            path.append(start) 
            path.reverse() 
            return path 

        closed_set.add(current)

        x, y = current 
        neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] 

        for nx, ny in neighbors: 
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0: 
                
                if (nx, ny) in closed_set:
                    continue                   # Skip Visited nodes

                new_cost = g_score[current] + 1 

                if (nx, ny) not in g_score or new_cost < g_score[(nx, ny)]: 
                    g_score[(nx, ny)] = new_cost 
                    f_score = new_cost + heuristic((nx, ny), goal) 

                    heapq.heappush(open_list, (f_score, (nx, ny))) 
                    came_from[(nx, ny)] = current 

    return None 


# ---------------- Main Program ---------------- 

rows = int(input("Enter number of rows: ")) 
cols = int(input("Enter number of columns: ")) 

print("Enter grid values (0 = free, 1 = obstacle):") 

grid = [] 
for i in range(rows): 
    row = list(map(int, input().split())) 
    grid.append(row) 

start = tuple(map(int, input("Enter start position (row col): ").split())) 
goal = tuple(map(int, input("Enter goal position (row col): ").split())) 

if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
    print("\nInvalid start or goal position")
else:
    path = astar(grid, start, goal) 

    if path: 
        print("\nShortest Path Found:") 
        for p in path: 
            print(p, end=" ") 
    else: 
        print("\nNo Path Found")
