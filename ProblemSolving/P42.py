# N Queen Problem
N=1

def check(row,column,pos):
  if column[row]>=0:
    return False
  
  if pos in column:
    return False 


  for i in range(row):
      if (abs(row-i) == abs(pos-column[i])) :
        return False
  

  return True
result=[]
def queen(row,columns):
  if row==N: 
    result.append(columns.copy())
    return

  for i in range(N):
    if check(row,columns,i):
      columns[row]=i
      queen(row+1,columns)
      columns[row]=-1

  return False


columns=[-1]*N
queen(0,columns)

answer=[]
for i in result:
  temp=[]
  for j in i:
    q = list("."*N)
    q[j]="Q"
    q= "".join(q)
    temp.append(q)
  answer.append(temp)

print(answer)
