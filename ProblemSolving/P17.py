# ag subsequence count
def subsequenceCount(A):
  count=0
  acount=0
  for x in A:
    if x =="g":
      count+=acount
    else:
      acount+=1
  
  return count

A ="gaggag"
print(subsequenceCount(A))