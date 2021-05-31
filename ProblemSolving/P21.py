# Multiplication of previous and next
# a) First element is replaced by multiplication of first and second. 
# b) Last element is replaced by multiplication of last and second last.

# Input 1:
#     A = [1, 2, 3, 4, 5]
# Output 1:
#     [2, 3, 8, 15, 20]

def multiplyPrevAndNext(A):

  multiplier=A[0]
  temp=A[0]
  
  for i in range(0,len(A)-1):
    if i==0:
      A[i]=temp*A[i+1]
    else:
      temp=A[i]
      A[i]= multiplier*A[i+1]
      multiplier=temp
      
  else:
    A[i+1]=multiplier*A[i+1]
  return A

A=[1, 2, 3, 4, 5]
print(multiplyPrevAndNext(A))
