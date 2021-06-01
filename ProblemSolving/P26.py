# Anti diagonal
# [ 
#   [1],
#   [2, 4],
#   [3, 5, 7],
#   [6, 8],
#   [9]
# ]
def antiDiagonal(A):

  top=0
  right=len(A)
  bottom=len(A)
  rowB=0
  left=0
  B=[[] for x in range(2*len(A)-1)] 

  while right-1>=0 and top<=len(A)-1 :
    
    for i in range(0,right):
       
      B[rowB].append(A[top][i])
      rowB+=1
    top+=1

    for i in range(top,bottom):
      B[rowB].append(A[i][right-1])
      rowB+=1
    right-=1
  
    left+=1
    rowB=left

  return B

A=[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(antiDiagonal(A))