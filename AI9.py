n=int(input('Enter value for N: '))
board=[]

for i in range(n):
    board.append([0]*n)
    
def isSafe(row,col):
    
    for i in range(row):
        if board[i][col]==1:
            return False
    
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    i=row-1
    j=col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True
    
        
def backtrack(row):
    
    if row==n:
        return True
    
    for col in range(n):
        if isSafe(row,col):
            board[row][col]=1
            
            if backtrack(row+1):
                return True
            
            board[row][col]=0
            
    return False




cols=[0]*n
d1=[0]*(2*n-1)
d2=[0]*(2*n-1)
    
def branch_bound(row):
    
    if row==n:
        return True
    
    for col in range(n):
        
        if cols[col]==0 and d1[row-col+n-1]==0 and d2[row+col]==0:
            board[row][col]=1
            d1[row-col+n-1]=1
            d2[row+col]=1
            cols[col]=1
            
            if branch_bound(row+1):
                return True
            
            board[row][col]=0
            d1[row-col+n-1]=0
            d2[row+col]=0
            cols[col]=0
            
    return False



print('For Backtracking choose 1')
print('For Branch and bound choose 2')
case=int(input('Enter your choice: '))

if case==1:
    backtrack(0)
elif case==2:
    branch_bound(0)

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            print('Q', end=" ")
        else:
            print('.', end=" ")
    print()