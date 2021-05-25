# Number of 1 Bits

class NumberOfBits:

  def countSetBits(self,A):
    count = 0
    for i in range(32):
      if A % 2 != 0:
        count = count+1
      
      A = A>>1
    return count

noOfBits = NumberOfBits()
print(noOfBits.countSetBits(5))
