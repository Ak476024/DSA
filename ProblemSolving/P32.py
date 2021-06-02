# unique Permutation of duplicates in a string

def Permutation(A,length,prefix):
  if len(prefix) ==length:
    print(prefix)

  
  for i in range(len(A)):
    if A[i]>0:
      B=A.copy()
      B[i]-=1
      Permutation(B,length,prefix=prefix+chr(i+97))
  return

A="abb"
B=[0]*26

for i in A:
  ascii=ord(i)- 97
  B[ascii]+=1

Permutation(B,len(A),"")

