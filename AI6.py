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

