# Pascal Triangle

#[
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

def pascalTriangle(A):
  B= [[0]*x for x in range(1,A+1)]

  B[0][0]=1

  for i in range(len(B))[1:]:
    for j in range(len(B[i])):
      if j == 0 or j==len(B[i])-1:
        B[i][j]=1
      else :
        B[i][j]=B[i-1][j-1]+(B[i-1][j] if j!=len(B[i-1])-1 else 1 )

  return B

print(pascalTriangle(5))