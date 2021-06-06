# Number of Squareful Arrays

# Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

# Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

A = [1,17.8]
sum=set()

import math
 

def isPerfectSquare(x):
    if (math.ceil(math.sqrt(x)) == math.floor(math.sqrt(x))):
      return True
    return False

def permutations(A,prefix,result):
  if len(prefix)==3:
    first = prefix[0]+prefix[1]
    second = prefix[1]+prefix[2]
    if isPerfectSquare(first) and isPerfectSquare(second):
      if first in sum:
        return
      else:
        result.append(prefix)
        sum.add(first)
    return

    
  for i in range(len(A)):
    permutations(A[:i]+A[i+1:],prefix+[A[i]],result)
  return

result=[]
permutations(A,[],result)
print(result)