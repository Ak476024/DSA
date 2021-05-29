#Add One To Number

def addOneToNumber(A):
  length = len(A)
  carry=0
  digit=0
  for i in range(length):
    cal=0
    if i==0:
     cal=(A[length-i-1]+1+carry)
    else:
      cal=(A[length-i-1]+carry)
    digit= cal%10
    carry= cal//10
    A[length-i-1]=digit
    if carry==0:
      break

  if carry==1:
    A.append(0)
    length+=1
    for i in range(length)[1:]:
      A[length-i-1]=A[length-i-2]
    A[0]=carry
  else:
    for i in range(length):
      if A[i] !=0:
        return A[i:]
  return  A

print(addOneToNumber([ 9,9,9 ]))