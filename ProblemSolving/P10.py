# Good Pair
# Given an array A and a integer B. A pair(i,j) in the array is a good pair if i!=j and (A[i]+A[j]==B).

# Input : A=[1,2,3,4] B = 7
# Output : 1

class GoodPair:

  def binarySearch(self,A,B,l=0,r=0):
    if(l>r):
      return False
    mid = int((l+r)/2)
    if A[mid]==B:
      return True
    elif A[mid]>B:
      self.binarySearch(A,B,l=l,r=mid-1)
    elif A[mid]<B:
      self.binarySearch(A,B,l=mid+1,r=r)
    return

  def check(self,A,B):
    length = len(A)
    if length<2 :
      return False
    index=0
    for element in A:
      index+=1
      if self.binarySearch(A,B-element,index,length-1):
        return True
    
    return False

A=[1,2,3,4] 
B = 7
gp = GoodPair()
print(gp.check(A,B))