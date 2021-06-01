# Search in a row wise and column wise sorted matrix

def binarySearch(A,B,start,end):
  if end>=start:
    mid = start +(end-start)//2
    if A[mid]== B:
      return mid
    elif A[mid]<B:
      return binarySearch(A,B,mid+1,end)
    if A[mid]>B:
      return binarySearch(A,B,start,mid-1)
  else:
    return -1
  

def getMinimum(A,i,j):
  J=j-1
  while True and J>=0:
    if A[i][j]!=A[i][J]:
      J+=1
      break
    else:
      J=j-1
  return J


def searchElement(A,B):
  row =len(A)
  col = len(A[0])
  for i in range(row):
    j=binarySearch(A[i],B,0,col-1)
    if j != -1:
      result=getMinimum(A,i,j)
      return (i*1009)+result
  else:
    return -1


A=[
[1, 2, 3,3,10,],
[4, 5, 6,10,12,],
[7, 8, 9,10,24],
]


print(searchElement(A,8))