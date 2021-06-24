def bubbleSort(A):
  temp = 0
  for i in range(len(A)):
    for j in range(len(A)-i-1):
      if A[j]>A[j+1]:
        temp=A[j]
        A[j]=A[j+1]
        A[j+1]=temp
  return

A=[1,3,4,5,0,9,6]
bubbleSort(A)
print(A)