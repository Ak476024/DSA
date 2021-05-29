# Multiple left rotations of the array


def getRotatedArray(A,rotations):
   for i in range(rotations):
    temp=A[0]
    for j in range(len(A))[1:]:
      A[j-1]=A[j]
    else:
      A[j]=temp

   return A

def leftRotation(A,B):
  B = [x%len(A) for x in B ]
  minRotate = min(B)
  rotations=[x-minRotate for x in B]

  print("rotation",rotations)
  
  rotatatedArray= getRotatedArray(A,minRotate)
  result=[]
  for x in range(len(B)):
    result.append(rotatatedArray)

  map={}
  map[0]=rotatatedArray
  for x in range(len(rotations)):
    if rotations[x] in map:
      result[x]=map.get(rotations[x])
    else:

     result[x]=map[rotations[x]]=getRotatedArray(result[x],rotations[x])
     print(result)

  return result



      