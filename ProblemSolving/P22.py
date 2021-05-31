# Primal Power
# Input: A = [-11, 7, 8, 9, 10, 11]
# output: 2

def primalPower(A):
  count=0
  for i in A:
    if i>1:
      for x in range(3,int((i/2)+1)):
        if i%x==0:
          break
      else:
          print(i)
          count=count+1
  return count

A = [-6, 10, 12]
print(primalPower(A))
