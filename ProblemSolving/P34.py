# Subset
# Input: A = [1, 2, 3]
# Output : 
# [
#  []
#  [1]
#  [1, 2]
#  [1, 2, 3]
#  [1, 3]
#  [2]
#  [2, 3]
#  [3]
# ]

def subset(A):
  result=[[]] 

  for i in A:
    result+= [e + [i] for e in result ]

  return result

A = [1, 2, 3]
print(subset(A))
