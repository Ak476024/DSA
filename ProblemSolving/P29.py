# Row with maximum number of ones

A = [   [1,1, 1, 1],
        [0,0, 1, 1],
        [0,0, 0, 1],
        [1,1, 1, 1]   
    ]


def maxOne(A):
  j=len(A)-1
  i=0
  max_i=0
  while j>=0 and i<=len(A)-1:
    if A[i][j]==1:
      j-=1
      max_i=i
    else:
      i+=1

  return max_i

print(maxOne(A))