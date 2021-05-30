# pattern printing

def printPattern(A):
  result=[[0]*A for i in range(A)]

  for i in range(A):
    for j in range(A-1,A-i-2,-1):
      result[i][j]=A-j

  return result

print(printPattern(3))
