# unique Permutation of a given string 

def permutation(A,prefix):
  if len(A)==0 :
    print(prefix,end=" ")
  
  for i in range(len(A)):
    permutation(A[:i]+A[i+1:],prefix+A[i])


  return

A="abcd"
permutation(A,"")
