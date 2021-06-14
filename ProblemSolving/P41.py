# Subsets II

def subsets(A):
  result=[[]]

  if len(A)==0 or A==None:
    return result
  
  for i in range(len(A)):
    for j in range(i,len(A)):
      result.append(A[i:j+1])

  
  return result

A=[1,2,2,2]
print(subsets(A))