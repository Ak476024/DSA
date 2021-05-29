# Spiral traversal

def spiral(A,row,column):
  
  top=0
  right=column
  bottom=row
  left=0
  while(left<=right and top<=bottom):  
    for i in range(left,right):
      print(A[top][i],end=" ")
    top+=1

    for i in range(top,bottom):
      print(A[i][right-1],end=" ")
    right-=1

    for i in range(right-1,left-1,-1):
      print(A[bottom-1][i],end=" ")
    bottom-=1

    for i in range(bottom-1,top,-1):
      print(A[bottom-1][left],end=" ")
    left+=1
  return


A=[
    [ 1, 2, 3,"a" ],
    [ 4, 5, 6,"b" ],
    [ 7, 8, 9,"c"], 
    [10,11,12,"d" ]
]

spiral(A,4,4)
