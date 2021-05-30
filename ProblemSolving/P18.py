# pattern printing

def printPattern(A):
  result=[[0]*A for i in range(A)]

  for i in range(A):
    for j in range(A,A-i-1,-1):
      result[i][j-1]=A-j+1

  return result

print(printPattern(4))