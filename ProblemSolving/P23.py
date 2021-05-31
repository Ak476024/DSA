# Spiral Order Matrix II

def spiralMatrix(A):
  A= [[0]*A for x in range(A)]

  top=0
  left=0
  right=len(A)
  bottom=len(A)
  count=0
  while left<=right and top<=bottom:

    for i in range(left,right):
      count+=1
      A[top][i]=count
    top+=1
    
    for i in range(top,bottom):
      count+=1
      A[i][right-1]=count
    right-=1

    for i in range(right-1,left-1,-1):
      count+=1
      A[bottom-1][i]=count
    bottom-=1

    for i in range(bottom-1,top-1,-1):
      count+=1
      A[i][left]=count
    left+=1
      
  return A


print(spiralMatrix(2))
